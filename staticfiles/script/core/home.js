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


    //scroll animations on features(why choose us) section-3
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
    // end animation scroll




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
    var pause = 5000; // The pause between each slide
    // var width = 15.75;
    var currentSlide = 1;
    var interval;

    function review() {
        let width = $('.section-4 .testimony').outerWidth() + 10;
        console.log('testimony width = ' + outerWidth);
        $('.testimony-container').animate({
            marginLeft: '-=' + width,

        }, animationSpeed, function() {
            currentSlide++;
            if (currentSlide >= ($('.testimony').length) - 1) {
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
    // end review slide




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