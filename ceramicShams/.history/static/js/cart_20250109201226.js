function addToCart(product_id) {

    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;
    console.log(`Product ID: ${product_id}, Count: ${count}`);

    $.ajax({
        type: "method",
        url: "url",
        data:{
            "product_id":product_id,
            "count":count
        }
        ,
        dataType: "dataType",
        success: function (response) {

        }
    });
}

