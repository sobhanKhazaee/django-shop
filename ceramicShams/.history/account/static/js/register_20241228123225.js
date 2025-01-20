$(document).on('click', '#show_pass', function () {
    $(this).hide();
    $("#hide_pass").show();
    $("#id_password").attr("type","text");

});