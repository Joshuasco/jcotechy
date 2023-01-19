$(document).ready(function() {

    //hero section
    let count = 0;
    let len = $('.hero-content-container').length;
    let hero_interval;


    function animate_hero() {
        if (count >= (len * 100)) {
            $('.hero-content-container').css({
                'transform': 'translateX(0)',
                'transition': 'all ease 0s',
            });
            count = 0;
        } else {
            $('.hero-content-container').css({
                'transform': 'translateX(-' + count + '%)',
                'transition': 'all ease .5s',
            });

            $('.hero-section .scroll-btn .btn').css('background-color', '');
        }
        count += 100;
        $('.hero-section .scroll-btn .btn:nth-child(' + (count / 100) + ')').css({
            'background-color': 'white',
            opacity: '.75'

        });

    }
    hero_interval = setInterval(animate_hero, 6000);


    $('.hero-section .scroll-btn .btn').each(function(i) {
        $(this).click(function() {
            clearInterval(hero_interval);
            count = i * 100;
            $('.hero-content-container').css({
                'transform': 'translateX(-' + count + '%)',
                'transition': 'all ease .5s',
            }).delay(5000);
            hero_interval = setInterval(animate_hero, 5000);
        });
    });

    //end hero section


    // begin service section
    // $('.services-action-btn').each(function() {

    //     let $this = $(this);
    //     $(this).click(function(e) {
    //         e.preventDefault();
    //         $(this).parents('.service-container').addClass('service-details')
    //             // $('body::before').css({
    //             //     backgroundImage: 'linear-gradient(to left, rgb(138, 43, 226, .5), rgb(138, 43, 226, .5))',
    //             //     zIndex: '3',
    //             // })
    //         $(this).parents('.service-container div').css({
    //             display: 'flex',
    //             padding: '.5em',
    //             justifyContent: 'center',
    //             alignItems: 'center',
    //             flexDirection: 'column',
    //         });
    //         $(this).parents('.service-container').children('.service-cancel-btn').toggle(250);
    //         $(this).parent('.service-description').toggle(250);
    //         $(this).parents('.service-description').siblings('.service-content').toggle(250);
    //         console.log('service clicked')
    //             // if(!$(this).parents('.service-container')){
    //             //     $parents('.service-container').css()
    //             // }
    //     });
    //     $(this).parents('.service-container').children('.service-cancel-btn').click(function() {
    //         $(this).toggle(250);
    //         $(this).parents('.service-container').removeClass('service-details');
    //         $(this).parents('.service-container').find('.service-description').toggle(250);
    //         $(this).parents('.service-container').find('.service-description').siblings('.service-content').toggle(250);
    //     });
    // });
    // end service section


    $('.faqs').click(function(e) {
        e.preventDefault();
        console.log("just cliked");
        $('html, body').animate({
            scrollTop: $("#faqs").offset().top
        }, 1000);
    });

    $('.hiws').click(function(e) {
        e.preventDefault();
        console.log("just cliked");
        $('html, body').animate({
            scrollTop: $("#hiws").offset().top
        }, 1000);
    });



    //scroll function for mobile device
    $(document).scroll(function() {
        let offsetT = $('.section-3').offset().top;
        let offsetH = $('.features').offset().height;
        let windowHeight = $(window).height();
        let scrolled = false;

        if ($(this).scrollTop() > 60) {
            $('.header-div').addClass('header-div-bg');
        } else {
            $('.header-div').removeClass('header-div-bg');
        }
        if ($(this).scrollTop() > (offsetT - 300) && !scrolled) {
            $('.features').addClass('active');
            console.log('active added');
            console.log(offsetT);
            console.log(windowHeight);
        }
    });



    // FAQS section
    $('.question').each(function() {
        $(this).click(function() {
            $(this).children('p').next('.reply').slideToggle();
            $(this).find('.btn-1').toggle();
            $(this).find('.btn-2').toggle();
            console.log("btn-1 clicked");
        });
    });





    //reviews
    var animationSpeed = 2000; // How quickly the next slide animates.
    var pause = 3000; // The pause between each slide
    var width = 100 / 3;
    var currentSlide = 1;
    var interval;

    function review() {

        $('.testimony-container').animate({
            marginLeft: '-=' + width + '%',

        }, animationSpeed, function() {
            currentSlide++;
            if (currentSlide >= ($('.testimony').length) - 3) {
                $('.testimony-container').css({ marginLeft: '0' });
                currentSlide = 0;
            }

        });

    }


    function startInterval() {
        interval = setInterval(review, pause);
    }

    function stopInterval() {
        clearInterval(interval);
    }

    $('.slider').on({
        'mouseleave': startInterval,
        'mouseenter': stopInterval,
    });
    startInterval();


    // testing Script
    // var animationSpeed = 1000; // How quickly the next slide animates.
    // var pause = 3000; // The pause between each slide.
    // var interval;

    // function startSlider() {
    //     $('.slides > li:first')
    //         .fadeOut(animationSpeed)
    //         .next()
    //         .fadeIn(animationSpeed)
    //         .end()
    //         .appendTo('.slides');

    // }
    // interval = setInterval(startSlider, pause);
    // $('.play').hide(); // Hiding the play button.
    // $('.pause').click(function() {
    //     clearInterval(interval);
    //     $(this).hide();
    //     $('.play').show();
    // });


    // end testing script



});