

$(document).ready(function () {

    //Materialize Nav Bar functions----------------
    $('.button-collapse').sideNav();

    //This hides the django feed back messages after 6 seconds----------
    setTimeout(function () {
        $('#dj-message').hide();
    }, 6000);


});


