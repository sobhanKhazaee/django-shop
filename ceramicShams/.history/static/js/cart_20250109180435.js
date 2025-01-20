function checkInputValue(product_id) {
    const countElement = document.getElementById('count_' + product_id);
    console.log("Input changed. New value:", countElement.value);
}

function addToCart(product_id) {
    console.log("this is product:" + product_id);
    const count = $('#count_' + product_id).val();
    console.log(count);
}