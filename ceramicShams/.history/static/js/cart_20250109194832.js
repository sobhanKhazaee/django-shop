$(document).on('change', 'input[type="number"]', function () {
    const product_id = $(this).data('product-id');
    const count = $(this).val();

    console.log(`Product ID: ${product_id}, Count: ${count}`);
});
function addToCart(product_id) {
    console.log("this is product:" + product_id);
    const count = $(`#count_${product_id}`).data('product-id') ? $(`#count_${product_id}`).val() : 1;
    console.log(count);
}

