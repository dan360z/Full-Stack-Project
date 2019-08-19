

$(document).ready(function () {

    //Materialize Nav Bar functions----------------
    $('.button-collapse').sideNav();

    //Modal----------------------------------------
    $('.modal').modal();

    //This hides the django feed back messages after 6 seconds----------
    setTimeout(function () {
        $('#dj-message').hide();
    }, 6000);


    //This shows the ticket details when a user hovers over the ticket------
    $('.details').hide();

    $('.ticket').hover( function() {
        $(this).find('.details').slideToggle();
    });



});


