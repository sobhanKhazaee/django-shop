$(document).on('click', '.submenu_btn', function () {
    if ($('.submenu').is(":visible")) {
        $('.submenu').slideDown(200);
    } else {
        $('.submenu').slide(200);
    }
});