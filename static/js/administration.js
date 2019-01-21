(function() {
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
	$('.raport-linker').on('click', function(){
		var id = '.'+$(this).attr('id');
		$('.raport:not(.invisible)').toggleClass('invisible');
		$(id).removeClass('invisible');
	});

      $('.add-btn1').on('click', function(e) { 
        var dishForm = $('.dishproduct-form.invisible');
        if(dishForm.length > 1) {
            dishForm.first().toggleClass('invisible');
        } else if(dishForm.length > 0) {
            dishForm.first().toggleClass('invisible');
            $(this).attr('disabled', 'disabled');
        }      


    });
      $('.add-btn2').on('click', function(e) { 
        var dishForm = $('.trans-form.invisible');
        if(dishForm.length > 1) {
            dishForm.first().toggleClass('invisible');
        } else if(dishForm.length > 0) {
            dishForm.first().toggleClass('invisible');
            $(this).attr('disabled', 'disabled');
        }      
  });
	     $('input, select, textarea').on('change', function() { 
       
       console.log('zajebioooza');
       var parent = $(this).parent().parent();
       if((parent.hasClass('update-form')||parent.hasClass('dish-form'))&&!parent.hasClass('edited')) parent.toggleClass('edited')
       console.log('zajebiooozawhoooj');
        parent.find("button").removeAttr("disabled");
 
    });
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

	             $('.changeColor').on('click', function(e) {
            if (confirm('Jesteś pewien, że chcesz zmienić szablon serwisu?')) {
                if (readCookie('template')) eraseCookie('template');
                createCookie('template', this.id, 30);
                
					location.reload();
                
            }
        });

})(jQuery);