$(document).ready(function() {
    console.log('ready');

    $('.article .stats-container .article-stats').each(function() {
        $(this).click(function(e) {
            // $('.article').preventDefault();
            // e.preventDefault();
            $(this).children('svg').toggle(250);
            // $('.stats-container svg:last-of-type').toggle(500);
            console.log('liked clicked')
        });
    });

});