$(document).on('click', '#show_pass', function () {
    $(this).hide();
    $("#hide_pass").show();
    $("#id_password").attr("type","text");
});
$(document).on('click', '#hide_pass', function () {
    $(this).hide();
    $("#show_pass").show();
    $("#id_password").attr("type","text");
});