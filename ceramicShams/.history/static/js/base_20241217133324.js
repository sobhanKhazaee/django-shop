$(document).on('click', '.submenu_btn', function () {
    if ($('.submenu').is(":visible")) {
        $('.submenu').hide(200);
        
    } else {
        $('.dashboar').show(200);
       
    }
});