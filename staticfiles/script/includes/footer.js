// $(document).ready(function () {

// });

$(function() {
    // scroll effect on subcrition
    $('.subscribe').click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#subscribe").offset().top
        }, 1000);
        $("#subscribe input").focus()
    });

    // end scroll effect on subscription
});