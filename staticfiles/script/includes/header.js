$(document).ready(function() {
    $('.account').click(function(e) {
        e.preventDefault();
    });





    let scrolled = false;
    //scroll function for mobile device
    if ($(document).scrollTop() > 80) {
        $('.header-div').addClass('header-div-bg');
        $('.header-div a').css('color', '#FD21CA');
        $('.socials').addClass('social-contact');
    } else {
        $(document).scroll(function() {
            if ($(this).scrollTop() > 80) {
                // $('.header-div').addClass('header-div-pos');
                $('.header-div').addClass('header-div-bg');
                $('.header-div a').css('color', '#FD21CA');
                $('.socials').addClass('social-contact');
            } else {
                // $('.header-div').removeClass('header-div-pos');
                $('.header-div').removeClass('header-div-bg');
                $('.socials').removeClass('social-contact')
                $('.header-div a').css('color', 'white');
            }
        });
    }



    // tablet and mobile view
    $('.menu-icon').click(function() {
        $('.header').slideToggle(250);
        $('.mobile-header .menu-icon').toggle(250);
    });
    $('.search-icon').click(function() {
        $(' .search-icon').toggle(250);
        $(' .search-field').slideToggle(250);
        // if($('.search-field').width =='80%'){
        //     $('.search-field').css('width','10%')
        // }
    });
    $('.account').click(function(e) {
        e.preventDefault();
        $('.account-dropdown').slideToggle(500)
    })
});