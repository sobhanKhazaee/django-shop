function add_to_cart(product_id) {
    const count = $("count" + product_id).val();
    cl
    $.ajax({
        url: '/cart/add-to-cart/?product_id=' + product_id & 'count=' + count,
        type: 'GET',
        data: {
            'product_id': product_id,
            'count': count
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