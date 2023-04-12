$(document).ready(function() {
    $('.account').click(function(e) {
        e.preventDefault();
    });

    let scrolled = false;
    //begin header background animation on scroll > 80
    // if ($(document).scrollTop() > 80) {
    //     $('.header-div').addClass('header-div-bg');
    //     $('.header-div a').css('color', '#FD21CA');
    //     $('.header-div .social-contacts').addClass('social-contact-bg');
    // } else {

    $(document).scroll(function() {
        if ($(this).scrollTop() > 80) {
            $('.header-div').addClass('header-div-bg');
            $('.header-div a').css('color', '#FD21CA');
            $('.header-div .social-contacts').addClass('social-contact-bg');
            if ($('.header-div .social-contacts').css('max-height') != '5em') {
                $('.header-div .social-contacts').css({ 'max-height': '5em', 'transition': '.5s all linear' });
            }
        } else {
            $('.header-div').removeClass('header-div-pos');
            $('.header-div').removeClass('header-div-bg');
            $('.header-div .social-contacts').removeClass('social-contact-bg')
            $('.header-div a').css('color', 'white');
            if ($('.header-div .social-contacts').css('max-height') != '0') {
                $('.header-div .social-contacts').css({ 'max-height': '0', 'transition': '.5s all linear' });
            }
        }
    });

    // }
    //end header background animation on scroll > 80



    // tablet and mobile view
    $('.menu-icon').click(function() {
        $('.header').slideToggle(250);
        $('.mobile-header .menu-icon').toggle(250);
    });
    $('.search-icon').click(function() {
        $(' .search-icon').toggle(250);
        $(' .search-field').slideToggle(250);
        $(' .search-field').focus().css('border-color', 'purple');
    });


    $('.account').click(function(e) {
        e.preventDefault();
        $('.account-dropdown').slideToggle(500)
    })

    // go to FAQS section in home page
    $('.faqs').click(function(e) {
        console.log("just cliked");
        $('html, body').animate({
            scrollTop: ($("#faqs").offset().top - 50)
        }, 1000);
    });
    //end FAQS section

    // Go to Service section in home page
    $('.services').click(function(e) {
        $('html, body').animate({
            scrollTop: ($("#services").offset().top - 50)
        }, 1000);
    });
    //End SErvice section

    //begin search form 
    $(".search-input").keypress(function(e) {
        let keycode = (e.keyCode ? e.keyCode : e.which);
        console.log('key pressed = ' + keycode);
        if (keycode == '13') {
            $(this).parent('form').submit();
        }
    });
    //end search form

});