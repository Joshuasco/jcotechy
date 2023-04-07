$(document).ready(function() {

    //begin contact-socials background animation effect
    $(document).scroll(function() {
        if ($(this).scrollTop() > 80) {
            $('.contact-socials .social-contacts').addClass('social-contact-bg');
        } else {
            $('.contact-socials .social-contacts').removeClass('social-contact-bg')
            $('.header-div a').css('color', 'white');
        }
    });
    //end contact-socials background animation effect





    // let elasticEmailPwdCreadential = "8D9BD376E99D59FCB4C68887D26DD9C96E3A";
    // $('#myform .submit').click(function(event) {
    //     event.preventDefault();
    //     Email.send({
    //         SecureToken: " ab122e9e-a6ef-4de9-8671-f324c4962a9a",
    //         To: 'them@website.com',
    //         From: "josh",
    //         Subject: "This is the subject",
    //         Body: "And this is the body"
    //     }).then(
    //         message => alert(message)
    //     );
    // Email.send({
    //     Host: "smtp.elasticemail.com",
    //     Username: "emekaodigbo1@gmail.com",
    //     Password: creadential,
    //     To: 'joshuaodigbo1@gmail.com',
    //     From: "emekaodigbo1@gmail.com",
    //     Subject: "This is the subject",
    //     Body: "And this is the body" 
    // }).then(
    //     message => alert(message)
    // );
    // });
    $('#contact-form').submit(function(event) {
        event.preventDefault(); // prevent the default form submission
        let url = window.location.href;
        console.log("this is my current location = " + url);
        //get form datas
        // get input value based on name attribute
        let first_name = $('input[name="first_name"]').val();
        let last_name = $('input[name="last_name"]').val();
        let email = $('input[name="email"]').val();
        let subject = $('input[name="subject"]').val();
        let message = $('input[name="message"]').val();
        message = $('input[name="message"]').html("<div><b>" + first_name + " " + last_name + "</b><br>" + message + "</div>");
        let body = message
            //end get form datas
        Email.send({
            SecureToken: " ab122e9e-a6ef-4de9-8671-f324c4962a9a",
            To: 'emekaodigbo1@gmail.com',
            From: email,
            Subject: subject,
            Body: body
        }).then(
            message => alert(message)
        );
        //end get form datas


        // submit the form data to the first action link
        $.post('http://127.0.0.1:8000/contact/', $(this).serialize(), function(data) {
            $('.msg-alert-container-1').slideToggle(250);
            $('.msg-alert-container-1 #msg-alert').text('thank your for reaching out to us, we will get back to you shortly through your mail');
        });

        // submit the form data to the second action link formspree
        $.post("https://formspree.io/f/xqkolkzw", $(this).serialize(), function(data) {});

        // do other stuff after the form submission
        // ...
    });
});