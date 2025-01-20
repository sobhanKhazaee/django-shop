
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
    const productId = $(this).data('product-id');
    const countElement = document.getElementById('count_' + productId);

    if (!countElement) {
        console.error('Input element not found for product ID:', productId);
        return;
    }

    const count = countElement.value;
})