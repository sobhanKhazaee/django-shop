//اسلایدر محصولات
$(".ModuleProduct1").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    rtl:true,
    autoplay: ,
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