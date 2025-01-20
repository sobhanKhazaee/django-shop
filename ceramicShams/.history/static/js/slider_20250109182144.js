$(".ModuleProduct1").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplayTimeout: 5000,
    autoWidth: true,
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