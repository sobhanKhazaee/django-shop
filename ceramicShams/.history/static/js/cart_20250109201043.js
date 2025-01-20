function addToCart(product_id) {
    // انتخاب از میان آیتم‌های اصلی (غیرکلون‌شده)
    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;
    console.log(`Product ID: ${product_id}, Count: ${count}`);

    $.ajax({
        type: "method",
        url: "url",
        data: "data",
        dataType: "dataType",
        success: function (response) {
            
        }
    });
}

