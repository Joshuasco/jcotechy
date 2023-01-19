$(document).ready(function() {

    $('.get-quote').click(function(e) {
        e.preventDefault();
        console.log('base clicked');
        $('.get-quote-form-container ').css({
            zIndex: '3',
            position: 'absolute',
            transition: '.5s linear',
        });
        $('html, body').animate({
            scrollTop: 0
        }, 500);
        $('.get-quote-form').slideToggle(500);
        $('.get-quote-form').css({
            transform: 'scale(1)',
            transition: '1s linear',
        })

    })
    $('.cancel-get-quote').click(function() {

        $('.get-quote-form').css({
            transform: 'scale(0)',
            transition: '1s linear',
        });
        $('.get-quote-form-container ').css({
            zIndex: '0',
            transition: '.5s linear',
            position: 'relative',
        });
        $('.get-quote-form').slideToggle(500);
    });

})