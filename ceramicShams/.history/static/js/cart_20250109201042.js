function addToCart(product_id) {
    // انتخاب از میان آیتم‌های اصلی (غیرکلون‌شده)
    const count = $(`.owl-item:not(.cloned) #count_${product_id}`).val() || 1;
    console.log(`Product ID: ${product_id}, Count: ${count}`);

    aj
}

