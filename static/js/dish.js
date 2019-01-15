(function() {
    //szablon
	

   $('input, select, textarea').on('change', function() { 
       
       console.log('zajebioooza');
       var parent = $(this).parent().parent();
       if((parent.hasClass('update-form')||parent.hasClass('dish-form'))&&!parent.hasClass('edited')) parent.toggleClass('edited')
       console.log('zajebiooozawhoooj');
        parent.find("button").removeAttr("disabled");
 
    });
   $('.save.btn').on('click', function(e) { 
       e.preventDefault();      
       
        $("#overlay").toggleClass('hidden');
       console.log('zajebioooza');
       $('.edited').submit();


    });
      $('.add-btn').on('click', function(e) { 
        var dishForm = $('.dish-form.invisible');
        if(dishForm.length > 1) {
            dishForm.first().toggleClass('invisible');
        } else if(dishForm.length > 0) {
            dishForm.first().toggleClass('invisible');
            $(this).attr('disabled', 'disabled');
        }      


    });



})(jQuery);