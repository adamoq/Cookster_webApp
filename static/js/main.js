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
	
	//FORMULARZE!!!!!!!!!!
	$('form.update-form').submit( function(e) {
		e.preventDefault();
		var id = $(this).attr('id');
		if( id.charAt(0) == 'c')
			{
			 id = id.substr(1);
			}		
			
		var url;
		if (typeof $(this).attr('data-target') !== 'undefined' ) url = window.location.protocol + "//" + window.location.host + "/" + $(this).attr('data-target')+id+'/';
		else url = window.location.protocol + "//" + window.location.host + "/menu/";
		
		var data = objectifyForm($(this).serializeArray())
		data['id'] = id;
		data = JSON.stringify(data);
		console.log('data'+data);
		
		console.log(id);
		$.ajax({
			url:url,
			type: 'PUT',
			contentType: 'application/json',
			data: data,
			success: function() {
					location.reload();
				}
			})
	});
	$('.button-remove').on('click', function() { //usunięcie obiektu
	
		var id = $(this).attr('id');
		if( id.charAt(0) == 'c')
			{
			 id = id.substr(1);
			}
		var url;
		if ($(this).attr('data-target') != 'undefined' ) url = window.location.protocol + "//" + window.location.host + "/" + $(this).attr('data-target')+id+'/';
		else url = window.location.protocol + "//" + window.location.host + "/menu/";
		
			
		if (confirm('Jesteś pewien, że chcesz usunać pracownika z bazy?')) {
			$.ajax({
				url: url,
				type: 'DELETE',
				contentType: 'application/json',
				processData: false,
				success: function() {
					location.reload();
				}
			})

		} else {
			console.log('error while removing');
		}
	})
	$('a#reset').on('click', function() { //reset obiektu
	console.log('xddd');
		var id = $(this).attr("href");
		if( id.charAt(0) == 'c')
			{
			 id = id.substr(1);
			}
		var url;
		if ($(this).attr('data-target') != 'undefined' ) url = window.location.protocol + "//" + window.location.host + "/" + $(this).attr('data-target')+id+'/';
		else url = window.location.protocol + "//" + window.location.host + id;
		
			
		if (confirm('Jesteś pewien, że chcesz zresetować hasło pracownika?')) {
					location.reload();
		} else {
			console.log('error while resetting');
		}
	})
	$('.edit').on('click',function(e){
		
		parentEl = $(this).parent().find('.id');
		var id = parentEl.html();console.log('ok'+id);
		id = '.modal'+id;console.log('ok'+id);
		$(id).modal('show');
	});				

	$('.modal-close').on('click', function(e){
		var id = '.modal'+$(this).attr('id');			
		$(id).modal('hide');
	});
	

    //DANIA

    if ($("#dishes-flag").length > 0) {
		console.log('XDDDDD');
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
			 $("#overlay").toggleClass('hidden');
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
				success: function() {
                        $("#overlay").toggleClass('hidden');
                    }
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

    }
    //PRACOWNICY
    else if ($("#employers-flag").length > 0) {
				
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
		
		$('.edit').on('click',function(e){
		
			parentEl = $(this).parent().parent().find('.id');
			var id = parentEl.html();console.log('ok'+id);
			window.location = '/dish/?d='+id;
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