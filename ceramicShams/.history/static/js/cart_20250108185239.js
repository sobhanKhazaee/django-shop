function add_to_cart(product_id) {
    $.ajax({
        url: '/cart/add',
        type: '',
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