$(document).ready(function() {
    // variable declaration
    let win_height, comment_url, reply_id, author, comment_id;
    comment_url = $('.comment-form').attr('action');
    const c_url = comment_url;
    //end variable declaration

    // article section
    $('.section-4 .react').each(function() {
        $(this).click(function(e) {
            // e.preventDefault();
            $(this).children('svg').toggle(250);
            console.log('react btn just clicked');
        });
    });
    $('.article-comment').click(function() {
            $('.section-5').slideToggle(500);
        })
        //end article section


    // comment section
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
    setInterval(getHeight, 2000);

    $('.comment-header button').click(function() {
        $('.section-5').slideToggle(500);
    });


    $('.section-5 .view-replies').each(function(i, v) {
        $(this).click(function() {
            $(this).parents('.comment-container').siblings('.comment-replies').slideToggle(500);
            // css({
            //     maxHeight: '50em',
            //     overflow: 'scroll',
            //     transition: '.5s',
            // });
        });

    });

    $('.section-5 .reactions .comment-reply').each(function(i, v) {
        $(this).click(function() {
            console.log('just cliked replycomment');
            comment_id = $(this).attr('comment_id');
            author = $(this).attr('author');

            if ($(this).attr('reply_id')) {
                reply_id = $(this).attr('reply_id');
                // comment_id = $(this).attr('reply_id');
            }
            comment_url = $('.comment-form').attr('action');
            // update comment url
            $('.comment-form').attr('action', c_url + '?comment_id=' + comment_id);
            comment_url = $('.comment-form').attr('action');
            // $('#comment-container').animate({
            //     scrollTop: $("#get_id").offset().top
            // }, 1000);
            $('.comment-form #id_content').val('@' + author + ' ' + comment_url);
        });
    });
    $('.comment-form .submit_comment').click(function(e) {
        e.preventDefault();
        console.log($('.comment-form').attr('action'));
        $('.comment-form').submit();

    })



    $('.faqs').click(function(e) {
        e.preventDefault();
        console.log("just cliked");
        $('html, body').animate({
            scrollTop: $("#faqs").offset().top
        }, 1000);
    });







    // begin ajaz post request
    $.post(
        post_title + '/comment/' + comment_id + '/likes', {},
        function(response) {
            // success condition


            console.log(response)
        }

    ).fail(function(xhr, textStatus, errorThrown) {


        console.log('You must be logedin to like, reply, edit or delete comment');
        console.log(xhr);
        console.log(textStatus);
        console.log(errorThrown)
    });
    // end ajax post request


    // begin ajax request
    $.ajax({
        url: post_title + '/comment/' + comment_id + '/edit',
        type: 'POST',
        data: { 'comment': getreplyComment },
        timeout: '2s',
        dataType: 'json',
        success: function(response) {
            // if successful, update comment. 
            console.log("comment updated");
            commentLocation.text(response.comment);
            replyForm.toggle(500);
        },
        error: function() {
            $('.likeError').show(500);
            console.log('request hindered, an error just occured');
        },
        complete: function() {
            console.log('request completed')
        },
    });
    // end ajax request




});