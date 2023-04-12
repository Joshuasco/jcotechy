$(document).ready(function() {


    //begin social share effect background animation on scroll > 80
    $(document).scroll(function() {
        if ($(this).scrollTop() > 80) {
            $('.social-shares').addClass('social-shares-bg');
        } else {
            $('.social-shares').removeClass('social-shares-bg')
        }
    });
    //end socail share effect background animation on scroll > 80

    // variable declaration
    let win_height, comment_url, reply_id, author, comment_id;
    comment_url = $('.comment-form').attr('action');
    const c_url = comment_url;
    //end variable declaration

    // begin .section-1 .article-header-icons audio player
    $(".article-header-icons .play").click(function() {
        let url = $('.play').attr('url');
        $('.audio').toggle(250);
        audio = document.getElementById('audio');

        if (audio) {
            audio.play();
            $("#article-audio audio").css('display', 'block');
            return false
        }
        $.get("http://" + url,
            function(data, textStatus, jqXHR) {
                url = $("#article-audio").attr('url');
                if (window.location.href.indexOf('https') >= 1) {
                    url = "https://" + url;
                } else {
                    url = "http://" + url;
                }
                console.log('audio url = ' + url);

                var audio = $('<audio  >', {
                    id: 'audio',
                    // hidden: true,
                    controls: 'controls',
                    autoplay: 'autoplay',
                    //   loop : 'loop',
                    preload: 'auto',
                    src: url
                });
                $("#article-audio").html(audio);
                $("#article-audio audio").css('display', 'block');
            }
        );
    });

    $(".article-header-icons .pause").click(function() {
        let url = $('.play').attr('url');
        document.getElementById('audio').pause();
        $('.audio').toggle(250);
        $("#article-audio audio").css('display', 'none');

    });

    // end .section-1 .article-header-icons

    // begin section-4 reactions
    $('.section-4 .react').each(function() {
        $(this).click(function(e) {
            $(this).children('svg').toggle(250);
            console.log('react btn just clicked');
        });
    });

    //begin share article
    $('.share-icon').click(function() {
        $(".social-shares").slideToggle(250);
        $(".social-shares").css('display', 'flex');
    });

    $(".social-shares .share").each(function() {
        $(this).click(function(e) {
            e.preventDefault();
            let href = $(this).attr('href');
            let url = $(this).attr('url')
            console.log("href = " + href);
            console.log("url = " + url);

            if (window.location.href.indexOf('https') >= 1) {
                url = "https://" + url;
            } else {
                url = "http://" + url;
            }

            $.get(url, function() {
                console.log("shared");
                window.open(href, '_blank', 'noopener', 'noreferrer');
            });

            // window.location.href = href
        });
    });

    //end share article 

    // copy url
    $('#copy-link').click(function(e) {
        e.preventDefault();
        // Create a temporary input element and set its value to the current URL
        let url = $(this).attr('href');
        var tempInput = $('<input>').val(url).appendTo('body').select();
        var tempInput = $('<input>').val(window.location.href).appendTo('body').select();
        // Copy the selected text to the clipboard
        document.execCommand('copy');
        // Remove the temporary input element
        tempInput.remove();
        $('.msg-alert-container-1').slideToggle(250);
        $('.msg-alert-container-1 #msg-alert').text('URL copied successfully');
    });
    // end  section-4 reactions

    // comment section
    // scroll to comment section on article-comment click
    $('.article-comment').click(function() {
            $('html, body').animate({
                scrollTop: $("#comment-section").offset().top - 100
            }, 1000);
        })
        //end scroll to comment section
    $('.section-5').css({
        maxHeight: (win_height),
        overflow: 'hidden',
    });

    function getHeight() {
        win_height = $(window).height();
        $('#comment-container').css({
            maxHeight: (win_height - 250),
        });
        console.log('done ')
    }
    // setInterval(getHeight, 2000);


    $('.section-5 .view-replies').each(function(i, v) {
        $(this).click(function() {
            $(this).parents('.comment-container').siblings('.comment-replies').slideToggle(500);
        });
    });

    $('.section-5 .reactions .comment-reply').each(function(i, v) {
        $(this).click(function() {
            // console.log('just cliked replycomment');
            // comment_id = $(this).attr('comment_id');
            author = $(this).attr('author');

            if ($(this).attr('reply_id')) {
                reply_id = $(this).attr('reply_id');
            }
            comment_url = $('.comment-form').attr('action');
            // update comment url
            $('.comment-form').attr('action', c_url + '?comment_id=' + comment_id);
            comment_url = $('.comment-form').attr('action');
            $('.comment-form #id_content').val('@' + author);
        });
    });
    $('.comment-form .submit_comment').click(function(e) {
        e.preventDefault();
        console.log($('.comment-form').attr('action'));
        $('.comment-form').submit();

    })


    // begin ajaz post request
    // $.post(
    //     post_title + '/comment/' + comment_id + '/likes', {},
    //     function(response) {
    //         // success condition

    //         console.log(response)
    //     }

    // ).fail(function(xhr, textStatus, errorThrown) {

    //     console.log('You must be logedin to like, reply, edit or delete comment');
    //     console.log(xhr);
    //     console.log(textStatus);
    //     console.log(errorThrown)
    // });
    // end ajax post request


    // begin ajax request
    // $.ajax({
    //     url: post_title + '/comment/' + comment_id + '/edit',
    //     type: 'POST',
    //     data: { 'comment': getreplyComment },
    //     timeout: '2s',
    //     dataType: 'json',
    //     success: function(response) {
    //         // if successful, update comment. 
    //         console.log("comment updated");
    //         commentLocation.text(response.comment);
    //         replyForm.toggle(500);
    //     },
    //     error: function() {
    //         $('.likeError').show(500);
    //         console.log('request hindered, an error just occured');
    //     },
    //     complete: function() {
    //         console.log('request completed')
    //     },
    // });
    // end ajax request


    // share article
    // $('#share-on-instagram').click(function() {
    //     let base = "https://www.facebook.com/sharer.php?u"
    //     let url = $windows.location.href();
    //     let instagram_share_url = base + url;
    //     console.log("url=" + url)
    //     console.log(instagram_share_url)
    // });
    // end share article


    // copy link
    // <!-- JavaScript code to handle the copy event -->

    // $('#copy-link').click(function(event) {
    //     event.preventDefault();
    //     var link = this.href;
    //     document.execCommand('copy');
    //     window.alert('url copied successfully');
    //     navigator.clipboard.writeText('copied finally').then(function() {
    //         alert('Link copied to clipboard');
    //     }, function() {
    //         alert('Error copying link to clipboard');
    //     });
    // });
    // end copy link

});