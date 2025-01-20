function addToCart(product_id) {
    const count = $('#            <section>
              <input type="number" min="1" id="count{{ product.id }}" value="1" />
              <button onclick="addToCart({{ product.id }})">
                افزودن به سبدخرید
              </button>
            </section>
          </div>')
    console.log(count);
    // $.ajax({
    //     url: '/cart/add-to-cart/?product_id=' + product_id & 'count=' + count,
    //     type: 'GET',
    //     data: {
    //         'product_id': product_id,
    //         'count': count
    //     },
    //     success: function (response) {
    //         if (response.status) {
    //             alert('Product added to cart');
    //         } else {
    //             alert('Product not added to cart');
    //         }
    //     }
    // });

}