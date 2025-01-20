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
        dataType: "json",
        success: function (response) {
            alert(response.success || "محصول با موفقیت به سبد خرید اضافه شد.");
            console.log();
        }, error: function (xhr) {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error);
        }
    });
}

