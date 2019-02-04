(function() {
    //szablon



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
    };
$('a').on('click', function(e) {

    $("#overlay").toggleClass('overlay-hidden');

});
$('.nav-bar.left a').on('click', function(e) {
    $( ".nav-bar.left li" ).each(function( index ) {
  if($( this ).hasClass('active')) $( this ).toggleClass('active');
});
    $(this).children('li').addClass('active');

});



	//FORMULARZE!!!!!!!!!!
		$('form.form2').submit( function(e) {
		e.preventDefault();
		var url;
		if (typeof $(this).attr('data-target') !== 'undefined' ) url = window.location.protocol + "//" + window.location.host + "/" + $(this).attr('data-target');


		var data = objectifyForm($(this).serializeArray())

		data = JSON.stringify(data);
		console.log('data'+data);

		console.log(id);
		$.ajax({
			url:url,
			type: 'POST',
			contentType: 'application/json',
			data: data,
			success: function() {
					location.reload();
				}
			})
	});

	$('form.update-form').submit( function(e) {
		e.preventDefault();
		var id = $(this).attr('id');
        var isTranslation = false;
        var url = window.location.protocol + "//" + window.location.host + "/" + $(this).attr('data-target');
        if ($(this).hasClass('trans-form')) isTranslation = true;
        if (id != null){
		if( id.charAt(0) == 'c' || id.charAt(0) == 'p' || id.charAt(0) == 'd' || isTranslation || $(this).hasClass('dishproduct-form'))
			 id = id.substr(1);
		console.log('ok'+isTranslation);

		if (typeof $(this).attr('data-target') !== 'undefined' ) url = url+id+'/';
		}
		var data = objectifyForm($(this).serializeArray())
		var type = 'POST';
        if($(this).hasClass('dishproduct-form')){
            data['dish'] = '/api/resdishes/'+data['dish']+'/';
            data['product'] = '/api/products/'+data['product']+'/';
            isTranslation = true;
            if (id != null)type = 'PUT';
        }else
		if (id != null){
            data['id'] = id;
            delete data['product'];
            delete data['dish'];
            type = 'PUT'}

        //restaurant details
        if(data['default_currency'] != null) {
            data['default_currency'] = '/api/currency/'+data['default_currency']+'/';
            data['default_lang'] = '/api/lang/'+data['default_lang']+'/';
            //isTranslation = True;
            //delete data['id'];
        }
		data = JSON.stringify(data);
		console.log('data'+data);

		console.log(id);
        if(isTranslation) var submitbutton = $(this).find("button[type=submit]");
		$.ajax({
			url:url,
			type: type,
			contentType: 'application/json',
			data: data,
			success: function() {

					if(isTranslation){
                        submitbutton.attr("disabled", "disabled");
}
                       if(! $("#overlay").hasClass('overlay-hidden')) $("#overlay").toggleClass('overlay-hidden');

				}
			})
	});
   $('.save-button').on('click', function() {

        $("#overlay").toggleClass('overlay-hidden');
        var id = $(this).attr('id');
        id = 'form#'+id;
        //$('#'+id).submit();
        //$('form#'+id).submit();

        console.log('submitting form22 id:'+id);
        $(this).parent().parent().find(id).submit();
        id = '.modal'+$(this).attr('id');
        $(id).modal('hide');

    });
  $('.save-button-post').on('click', function() {

        $("#overlay").toggleClass('overlay-hidden');
        $("#cookmodal").modal('hide');

    });

	$('.button-remove').on('click', function() { //usunięcie obiektu

        if($(this).parent().hasClass('new')) $(this).parent().remove();
        else {
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
			 $("#overlay").toggleClass('overlay-hidden');
            var data = objectifyForm(this);
            var id = data['id'];
            data = JSON.stringify(data);
            $.ajax({
                url: 'http://cookster-cookster.193b.starter-ca-central-1.openshiftapps.com/api/category/' + id + '/',
                type: 'PUT',
                contentType: 'application/json',
                data: data,
                dataType: 'json',
                processData: true,
				success: function() {
                        $("#overlay").toggleClass('overlay-hidden');
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


    }
})(jQuery);