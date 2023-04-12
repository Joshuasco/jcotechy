$(document).ready(function() {


    $('.info').each(function() {
        $(this).click(function() {
            $(this).children('.more').slideToggle();
            $(this).find('.btn-1').toggle();
            $(this).find('.btn-2').toggle();
            console.log("btn-1 clicked");
        });
    });

});