function addToCart(product_id) {
    base_url = "http://127.0.0.1:8000/"
    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;

    $.ajax({
        type: "GET",
        url: base_url + "cart/add-to-cart/",
        data: {
            "product_id": product_id,
            "count": count
        }
        ,
        dataType: "dataType",
        success: function (response) {
            alert(response.message || "محصول با موفقیت به سبد خرید اضافه شد.");
            location.reload();
        }, error: function (xhr) {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error || "مشکلی در افزودن محصول به سبد خرید وجود دارد.");
        }
    });
}

