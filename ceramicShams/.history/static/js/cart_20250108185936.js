function add_to_cart(product_id) {
    const count = $("")
    $.ajax({
        url: '/cart/add-to-cart/?product_id=' + product_id,
        type: 'GET',
        data: {
            'product_id': product_id,
            'quantity': 1
        },
        success: function (response) {
            if (response.status) {
                alert('Product added to cart');
            } else {
                alert('Product not added to cart');
            }
        }
    });

}