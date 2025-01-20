$(".ModuleProduct1").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplayTimeout: 5000,
    <input type="number" min="1" id="count_{{ product.id }}" value="1" />
<button type="button" class="add-to-cart-button" data-product-id="{{ product.id }}">
  افزودن به سبد خرید
</button>
    rtl: true,
    autoplay: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
});