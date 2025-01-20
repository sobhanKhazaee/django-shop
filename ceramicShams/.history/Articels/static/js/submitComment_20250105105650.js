$(document).ready(function () {
    $('#comment-form').submit(function (event) {
        event.preventDefault();
        var comment = $('#comment').val();
        var article_id = $('input[name="article_id"]').val();
        var parent_id = $("#parent_id").val() || "";  // گرفتن parent_id
        console.log(parent_id);

        $.ajax({
            type: 'POST',
            url: 'submit_comment',  // URL مربوط به ثبت نظر
            data: {
                'comment': comment,
                'article_id': article_id,  // ارسال آیدی مقاله به همراه داده‌ها
                'parent_id': parent_id,    // ارسال آیدی نظر والد
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                if (response.success) {
                    $('#comments-section').html(response.html);  // به‌روزرسانی نظرات
                    document.getElementById("").scrollIntoView({})
                    $('#comment').val('')  // خالی کردن فیلد نظر
                    alert("نظر شما با موفقیت ثبت شد");
                    if ($('#no_comment').is(':visible')) {
                        $('#no_comment').hide();
                    }
                } else {
                    $('#response').html('<p>' + response.message + '</p>');
                }
            },
            error: function () {
                $('#response').html('<p>خطا در ارسال نظر!</p>');
            }
        });
    });
});

$(document).on("click", ".reply_button", function (event) {
    event.preventDefault();
    var parent_id = $(this).attr("parent_id");  // گرفتن آیدی نظر والد
    $("#parent_id").val(parent_id);  // قرار دادن آیدی نظر والد در فیلد مخفی
    document.getElementById('write_comment').scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });
});
