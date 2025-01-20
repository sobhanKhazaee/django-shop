
    console.log("this is :" + product_id);
      // استفاده از jQuery برای گرفتن مقدار ورودی
      const countElement = document.getElementById('count_' + product_id);
      if (!countElement) {
          console.error('Input element not found for product_id: ' + product_id);
          return;
      }
  
      const count = countElement.value;
      console.log("Product Count: " + count);

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