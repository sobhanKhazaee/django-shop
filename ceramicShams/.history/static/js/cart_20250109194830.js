$(document).on('change', 'input[type="number"]', function () {
    const product_id = $(this).data('product-id');
    const count = $(this).val();

    console.log(`Product ID: ${product_id}, Count: ${count}`);
});


