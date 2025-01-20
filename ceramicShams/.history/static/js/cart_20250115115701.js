const base_url = "http://127.0.0.1:8000/"
$(d)
function addToCart(product_id) {
    $(event.target).siblings('.count_box').show(200);
    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;
    $.ajax({
        type: "GET",
        url: base_url + "cart/add-to-cart/",
        data: {
            "product_id": product_id,
            "count": count
        }
        ,
        dataType: "json",
        success: function (response) {
            // alert(response.success || "محصول با موفقیت به سبد خرید اضافه شد.");
            console.log(1);
        }, error: function (xhr) {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error);
        }
    });
}

function removeFromCart(product_id) {
    $.ajax({
        type: "GET",
        url: base_url + "cart/remove-from-cart/",
        data: {
            "product_id": product_id
        },
        dataType: "json",
        success: function (response) {
            $('.cart_content').html(response.html);
        }, error: function (xhr) {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error);
        }
    });
}

function addCount(product_id,state) {
    $.ajax({
        type: "GET",
        url: base_url + "cart/add-count/",
        data: {
            "product_id": product_id,
            "state":state
        },
        dataType: "json",
        success: function (response) {
            $('.cart_content').html(response.html);
        }, error: function (xhr) {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error);
        }
    });
}

// function reduceCount(product_id) {
//     $.ajax({
//         type: "GET",
//         url: base_url + "cart/reduce-count/",
//         data: {
//             "product_id": product_id
//         },
//         dataType: "json",
//         success: function (response) {
//             $('.cart_content').html(response.html);
//         }, error: function (xhr) {
//             const errorResponse = JSON.parse(xhr.responseText);
//             alert(errorResponse.error);
//         }
//     });
// }

