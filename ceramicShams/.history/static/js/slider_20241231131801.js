//اسلایدر محصولات
$(".ModuleProduct1").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplayTimeout: 5000,
    rtl: true,
    autoplay: true,
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