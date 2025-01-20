
function addToCart(product_id) {
    console.log("this is product:" + product_id);
    const count = $(`#count_${product_id}`).data('product-id') ? $(`#count_${product_id}`).val() : 1;
    console.log(count);
}

