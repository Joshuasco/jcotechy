$(document).ready(function() {
    // begin message alert
    // togglenclose message alert
    $(".msg-alert-container .close-msg-alert").click(function() {
        $('.msg-alert-container').slideUp(500);
    })
    $(".msg-alert-container-1 .close-msg-alert").click(function() {
            $('.msg-alert-container-1').slideUp(500);
        })
        // end message alert


    // begin django csrf-token for form submition
    //funtion to handle all ajax post request
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }

        }
    });

    // end django csrf-token for form submition


    // begin get quote form
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
    // end get quote form

})