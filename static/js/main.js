(function() {
    //szablon
    function createCookie(name, value, days) {
        var expires;

        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
    }

    function readCookie(name) {
        var nameEQ = encodeURIComponent(name) + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ')
                c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0)
                return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
        return null;
    }

    function eraseCookie(name) {
        createCookie(name, "", -1);
    }
    if (readCookie('template')) {
        var id = readCookie('template');
        switch (id) {
            case '0':
                $(':root').css('--colorAccent1', '#307E4A');
                $(':root').css('--colorAccent2', '#922429');
                $(':root').css('--colorAccent3', '#C98E1C');
                $(':root').css('--colorAccent4', '#5D5952');
                $(':root').css('--colorAccent5', '#513552');
                break;
            case '1':
                $(':root').css('--colorAccent1', '#FF3826');
                $(':root').css('--colorAccent2', '#B5271B');
                $(':root').css('--colorAccent3', '#00AEE8');
                $(':root').css('--colorAccent4', '#C1C1C1');
                $(':root').css('--colorAccent5', '#3A3535');
                break;
            case '2':
                $(':root').css('--colorAccent1', '#5BC0EB');
                $(':root').css('--colorAccent2', '#FDE74C');
                $(':root').css('--colorAccent3', '#9BC53D');
                $(':root').css('--colorAccent4', '#E55934');
                $(':root').css('--colorAccent5', '#FA7921');
                break;
            case '3':
                $(':root').css('--colorAccent1', '#011627');
                $(':root').css('--colorAccent2', '#9BC53D');
                $(':root').css('--colorAccent3', '#2EC4B6');
                $(':root').css('--colorAccent4', '#E71D36');
                $(':root').css('--colorAccent5', '#FF9F1C');
                break;
        }
			$(':root').css('--colorActive', '--colorAccent3');
    }



    function objectifyForm(formArray) { //serialize data function
        var returnArray = {};
        for (var i = 0; i < formArray.length; i++) returnArray[formArray[i]['name']] = formArray[i]['value'];
        return returnArray;
    }

    $("form input.not-active").on('click', function() {
        $(this).removeClass('not-active');
    })

    //DANIA

    if ($("#dishes-flag").length > 0) {
        //usuniecie kategorii z bazy
        $('.category-remove').on('click', function(e) { //usunięcie obiektu
            e.preventDefault();
            var id = $(this).val();
            if (confirm('Jesteś pewien, że chcesz tą usunać kategorię z bazy?')) {
                $.ajax({
                    url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/category/' + id + '/',
                    type: 'DELETE',
                    contentType: 'application/json',
                    dataType: 'json',
                    processData: false,
                    success: function() {
                        location.reload();
                    }
                })
            } else {
                // Do nothing!
            }
        })
        //update kategorii
        $(document).on('submit', 'form.category-form', function() {
            event.preventDefault();
            var data = objectifyForm(this);
            var id = data['id'];
            data = JSON.stringify(data);
            $.ajax({
                url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/category/' + id + '/',
                type: 'PUT',
                contentType: 'application/json',
                data: data,
                dataType: 'json',
                processData: false,
            })
        });
        $('.category-edit').on('click', function() {
            $(this).parent().parent().find('input[name="name"]').attr('disabled', false).removeClass('hidden');
            $(this).parent().parent().find('input[name="submit"]').attr('disabled', false).removeClass('hidden');
            $(this).parent().parent().addClass('active');
            $(this).parent().parent().find('a').hide();
        });

    }
    //PRODUKTY
    else if ($("#products-flag").length > 0) {
        //dodanie nowego produktu front-end
        $('.add-product').on('click', function() {
            $('table').append('<tr> <td width="90%"> <form class = "emplyee-form"> <div class="form-group"> <input type = "text" name = "id" class = "form-control not-active" value = "#" disabled="disabled"> </div> <div class="form-group"> <input type = "text" name = "name" class = "form-control"> <span class="glyphicon glyphicon-remove form-control-feedback"></span> </div> <div class="form-group"> <input type = "text" name = "surname" class = "form-control"> <span class="glyphicon glyphicon-remove form-control-feedback"></span> </div> <div class="form-group"> <select name = "position" class = "form-control not-active"> <option value = "0">Dostawca</option> <option value = "1">Kelner</option> <option value = "2">Kucharz</option> </select> <span class="glyphicon glyphicon-remove form-control-feedback"></span> </div> <div class="form-group"> <input type = "text" name = "login" class = "form-control"> <span class="glyphicon glyphicon-remove form-control-feedback"></span> </div> <div class="form-group"> <input type = "password" name = "password" class = "form-control"> <span class="glyphicon glyphicon-remove form-control-feedback"></span> </div> <input type = "image" name = "submit" class = "remove-icon not-active" src = "/static/img/accept-icon.png" disabled> </form> </td> <td width="5%"></td> </tr>');
            var el = $("form input[type='password']").last()[0];
            el.onmouseover = mouseoverPass;
            el.onmouseout = mouseoutPass;

            function mouseoverPass() {
                this.type = "text";
            }

            function mouseoutPass() {
                this.type = "password";
            }
        })
        //walidacja pól
        $(document).on('change', 'input', function() {
            var inputValue = $(this).val();
            var check = false;
            var acceptbutton = $(this).parent().parent().find('input:image').first();
            if (acceptbutton.hasClass('not-ready')) acceptbutton.removeClass('not-ready');
            if ($(this).attr('name') == 'name') check = /^[a-zA-ZąęćżóśźŻĆ]+$/.test(inputValue);
            if (check & $(this).parent().hasClass('has-feedback')) $(this).parent().addClass('has-warning has-feedback');
            if (!check & !$(this).parent().hasClass('has-feedback')) $(this).parent().removeClass('has-warning has-feedback');
            check = true;
            $(this).parent().parent().find('input:text').each(function() {
                if ($(this).parent().hasClass('has-warning') || $(this).val() == '') {
                    check = false;
                }
            })

            if (check) {
                acceptbutton.prop('disabled', false);
                if (acceptbutton.hasClass('not-active')) acceptbutton.removeClass('not-active');
            } else {
                acceptbutton.prop('disabled', true);
                if (!(acceptbutton.hasClass('not-active'))) acceptbutton.addClass('not-active');
            }

        });
        //update produktu
        $(document).on('submit', 'form.product-form', function() {
            event.preventDefault();
            var data = objectifyForm(this);
            var id = data['id'];
            data = JSON.stringify(data);
            $.ajax({
                url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/products/' + id + '/',
                type: 'PUT',
                contentType: 'application/json',
                data: data,
                dataType: 'json',
                processData: false,
            })


            $(this).parent().parent().find('input').each(function() {
                if (!($(this).hasClass('not-active'))) $(this).toggleClass('not-active');
                if ($(this).attr('type') == 'image') $(this).toggleClass('not-ready');
            });
        })
        //uzupełnienie formularza - wybranie dostępności produktu
        $('.radio-av').on('click', function() {
            $("input[name='av']").val($(this).val());;
            console.log('xdd');
        })
        $('.remove-icon').on('click', function(e) { //usunięcie obiektu
            e.preventDefault();
            var form = $(this).parent().parent().find('form').first()[0];
            console.log(form);

            var data = objectifyForm(form);
            var id = data['id'];
            if (confirm('Jesteś pewien, że chcesz usunać product: ' + data['name'] + ' z bazy?')) {
                $.ajax({
                    url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/products/' + id + '/',
                    type: 'DELETE',
                    contentType: 'application/json',
                    data: data,
                    dataType: 'json',
                    processData: false,
                    success: function() {
                        location.reload();
                    }
                })

            } else {
                // Do nothing!
            }
        })

    }
    //PRACOWNICY
    else if ($("#employers-flag").length > 0) {


        $(document).on('submit', 'form.emplyee-form', function() {
            event.preventDefault();
            var data = objectifyForm(this);
             //aktualizowanie obiektu
			 var id = data['id'];
            data = JSON.stringify(data);
            
			data['position'] = $(this).find('select').val();
            $.ajax({
                url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/resemployees/' + id + '/',
                    type: 'PUT',
                    contentType: 'application/json',
                    data: data,
                    dataType: 'json',
                    processData: false,
                })

            
            $(this).parent().parent().find('input').each(function() {
                if (!($(this).hasClass('not-active'))) $(this).toggleClass('not-active');
                if ($(this).attr('type') == 'image') $(this).toggleClass('not-ready');
            });
        })
        $('.remove-icon').on('click', function() { //usunięcie obiektu
            var form = $(this).parent().parent().find('form').first()[0];
            var data = objectifyForm(form);
            var id = data['id'];
            if (confirm('Jesteś pewien, że chcesz usunać pracownika ' + data['name'] + ' ' + data['surname'] + ' z bazy?')) {
                $.ajax({
                    url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/resemployees/' + id + '/',
                    type: 'DELETE',
                    contentType: 'application/json',
                    data: data,
                    dataType: 'json',
                    processData: false,
                    success: function() {
                        location.reload();
                    }
                })

            } else {
                // Do nothing!
            }
        })
        //skrypty dla form
        $('table tr').css('opacity', '1');
        var elems = document.querySelectorAll("form input[type='password']");
        [].forEach.call(elems, function(el) {
            el.onmouseover = mouseoverPass;
            el.onmouseout = mouseoutPass;
        });

        function mouseoverPass() {
            this.type = "text";
        }

        function mouseoutPass() {
            this.type = "password";
        }
        $("form input.not-active").on('click', function() {
            $(this).removeClass('not-active');
        })

        //walidacja wpisywanego tekstu
        $('.emplyee-form .form-group .pass, .emplyee-form .pass,.pass, input').on('change', function() {
            var inputValue = $(this).val();
			console.log('xDDD');
            var check = false;
            var acceptbutton = $(this).parent().parent().find('input:image').first();
			console.log('xDDD');
            if (acceptbutton.hasClass('not-ready')) acceptbutton.removeClass('not-ready');
            switch ($(this).attr('name')) {
                case 'name':
                case 'surname':
                    check = /^[a-zA-ZąęćżóśźŻĆ]+$/.test(inputValue);
                    break;
                case 'login':
                case 'password':
                    check = /^[a-zA-Z0-9]+$/.test(inputValue);
                    break;
            }
            if (check & $(this).parent().hasClass('has-feedback')) $(this).parent().toggleClass('has-warning has-feedback');
            if (!check & !$(this).parent().hasClass('has-feedback')) $(this).parent().toggleClass('has-warning has-feedback');
            check = true;
            $(this).parent().parent().find('input:text, input:password').each(function() {
                if ($(this).parent().hasClass('has-warning') || $(this).val() == '') {
                    check = false;
                }
            })

            if (check) {
                acceptbutton.prop('disabled', false);
                if (acceptbutton.hasClass('not-active')) acceptbutton.removeClass('not-active');
            } else {
                acceptbutton.prop('disabled', true);
                if (!(acceptbutton.hasClass('not-active'))) acceptbutton.toggleClass('not-active');
            }

        });
    } else if ($("#category-flag").length > 0) {
        $('.remove-icon').on('click', function(e) {
            var form = $(this).parent().parent().find('form').first()[0];
            var data = objectifyForm(form);
            var id = data['id'];
            if (confirm('Jesteś pewien, że chcesz usunać pracownika ' + data['name'] + ' ' + data['surname'] + ' z bazy?')) {
                $.ajax({
                    url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/resdishes/' + id + '/',
                    type: 'DELETE',
                    contentType: 'application/json',
                    data: data,
                    dataType: 'json',
                    processData: false,
                    success: function() {
                        location.reload();
                    }
                });
            };
        });
    } else if ($("#administration-flag").length > 0) {

        $('.changeColor').on('click', function(e) {
            if (confirm('Jesteś pewien, że chcesz zmienić szablon serwisu?')) {
                if (readCookie('template')) eraseCookie('template');
                createCookie('template', this.id, 30);
            }
        });
    } else if ($("#orders-waiter-flag").length > 0) {
		//przyporzadkowywanie taskow
		$('.orderdrag').each(function(){
			var str = $(this).attr('id');
			var pos = str.indexOf('.');
			var state = str.slice(pos+1);
			if (state == 1 ) $('#stage--step1').append($(this));
			if (state == 2 ) $('#stage--step2').append($(this));
		});
		
		//drag and drop
        function allowDrop(ev) {
            ev.preventDefault();
        }

        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
        }

        function drop(ev) {
            ev.preventDefault();
            var data = ev.dataTransfer.getData("text");
            ev.target.appendChild(document.getElementById(data));
        }
		
		//modal
		$('.order').on('click', function(){
			var id = '.ordermodal'+$(this).attr('id');
			
			$(id).addClass('in');
		});
		$('.modal-close').on('click', function(){
			var id = '.ordermodal'+$(this).attr('id');
			
			$(id).removeClass('in');
		});
    }
})(jQuery);