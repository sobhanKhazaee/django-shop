function addToCart(product_id) {
    base_url = "http://127.0.0.1:8000/"
    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;
    console.log(`Product ID: ${product_id}, Count: ${count}`);

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

        }
    });
}

