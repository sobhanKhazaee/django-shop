function toEnglishDigits(str) {
    return str.replace(/[۰-۹]/g, function (w) {
      return String(w.charCodeAt(0) - 1776);
    }).replace(/[٠-٩]/g, function (w) {
      return String(w.charCodeAt(0) - 1632);
    });
  }
function addToCart(product_id) {
    console.log("this is :" + product_id);
    const count = $('#count_'+product_id).val()
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