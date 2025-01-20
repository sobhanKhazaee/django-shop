$(document).ready(function() {
    $('#comment-form').submit(function(event) {
        console.log("clic");
        event.preventDefault();  // جلوگیری از ارسال فرم به صورت عادی
        var comment = $('#comment').val();
        
        // ارسال نظر از طریق AJAX
        $.ajax({
            type: 'POST',
            url: '{% url "submit_comment" %}',  // URL مربوط به ثبت نظر
            data: {
                'comment': comment,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.success) {
                    $('#response').html('<p>نظر شما با موفقیت ثبت شد!</p>');
                } else {
                    $('#response').html('<p>لطفاً ابتدا وارد حساب کاربری خود شوید.</p>');
                }
            },
            error: function() {
                $('#response').html('<p>خطا در ارسال نظر!</p>');
            }
        });
    });
});
