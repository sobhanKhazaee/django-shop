$(document).on('click', '.submenu_btn', function () {
    if ($('.submenu').is(":visible")) {
        $('.dashboar').hide(200);
        $('.main1').css('width', '100%');
    } else {
        $('.dashboar').show(200);
        $('.main1').css('width', '88%');
    }
});