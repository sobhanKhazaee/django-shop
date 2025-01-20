$(document).on('click', '.moblile_menu', function () {
    if ($('.dashboar').is(":visible")) {
        $('.dashboar').hide(200);
        $('.main1').css('width', '100%');
    } else {
        $('.dashboar').show(200);
        $('.main1').css('width', '88%');
    }
});