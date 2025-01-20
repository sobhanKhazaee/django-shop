
function addToCart(product_id) {
    console.log("this is product:" + product_id);
    const count = $('#count_' + product_id).val();
    console.log(count);
}

// ثبت رویداد کلیک به صورت داینامیک
function updateCount(productId) {
    const countElement = document.getElementById('count_' + productId);
    console.log("Updated Count for Product ID", productId, ":", countElement.value);
}

$(document).on('click', '.add-to-cart-button', function () {
    const product_id = $(this).data('product-id');
    const count = $('#count_' + product_id).val();

    console.log("Product ID:", product_id);
    console.log("Count:", count);
})