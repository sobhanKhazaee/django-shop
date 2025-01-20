$(document).ready(function () {
    $('#comment-form').submit(function (event) {
        event.preventDefault();
        var comment = $('#comment').val();
        var article_id = $('input[name="article_id"]').val();
        var parent_id = $("#parent_id").val()

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
                    if (parent_id == null && parent_id == "") {
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
                    } else {
                        // اگر پاسخ به یک نظر باشد
                        var parentComment = $(`#comment-${parent_id}`);
                        parentComment.find('.comment_details').append(`
                         <div class="comment_box reply" id="comment-${response.comment.created_at}">
                         <section class="comment_details">
                        <span>${response.comment.created_at}</span>
                         <span>${response.comment.user}</span>
                        </section>
            <br />
            <section>${response.comment.comment}</section>
        </div>
                    `);
                    }


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

$(document).on("click", ".reply_button", function (event) {
    event.preventDefault();
    var parent_id = $(this).attr("parent_id");
    $("#parent_id").val(parent_id)
    document.getElementById('write_comment').scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    })
})
