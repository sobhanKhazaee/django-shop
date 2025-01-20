$(document).ready(function() {
    $('#comment-form').submit(function(event) {
        event.preventDefault();  // جلوگیری از ارسال فرم به صورت عادی
        var comment = $('#comment').val();
        var article_id = $('input[name="article_id"]').val();  // دریافت آیدی مقاله از فیلد مخفی
        
        // ارسال نظر از طریق AJAX
        $.ajax({
            type: 'POST',
            url: '"submit_comment" %}',  // URL مربوط به ثبت نظر
            data: {
                'comment': comment,
                'article_id': article_id,  // ارسال آیدی مقاله به همراه داده‌ها
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.success) {
                    $('#response').html('<p>نظر شما با موفقیت ثبت شد!</p>');
                } else {
                    $('#response').html('<p>' + response.message + '</p>');
                }
            },
            error: function() {
                $('#response').html('<p>خطا در ارسال نظر!</p>');
            }
        });
    });
});
