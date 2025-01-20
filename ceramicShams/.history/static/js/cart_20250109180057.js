function addToCart(product_id) {
    console.log("this is product:" + product_id);
    const count = $('#count_'+product_id).val();
    console.log(count);
}