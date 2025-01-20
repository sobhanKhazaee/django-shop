$(document).ready(function () {
    $('#comment-form').submit(function (event) {
        event.preventDefault();
        var comment = $('#comment').val();
        var article_id = $('input[name="article_id"]').val();

        $.ajax({
            type: 'POST',
            url: 'submit_comment',  // URL مربوط به ثبت نظر
            data: {
                'comment': comment,
                'article_id': article_id,  // ارسال آیدی مقاله به همراه داده‌ها
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                if (response.success) {
                    var newComment = `
                         <div class="comment_box" id="comment-${response.comment.created_at}">
                            <section class="comment_details">
                                <span>${response.comment.created_at}</span>
                                <span>${response.comment.user}</span>
                            </section>
                            <br />
                            <section>${response.comment.comment}</section>
                        </div>
                    `;
                    $('#comments-section').prepend(newComment);
                    document.getElementById(`comment-${response.comment.created_at}`).scrollIntoView({
                        behavior: 'smooth',
                        block: 'center'
                    });
                    $('#comment').val('')
                    alert("نظر شما با موفقیت ثبت شد");
                    if ($('#no_comment').is(':visible')) {
                        $('#no_comment').hide();
                    };
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

$(document).on("click",".reply_button",function(event){
    event.preventDefault();
    var parent_id = $(this).attr("parent_id");
    console.log(parent_id);
    document.getElementById('parent_id')


})
