//اسلایدر محصولات
$(".ModuleProduct1").owlCarousel({
    loop:true,
    margin:10,
    nav:tr,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:5
        }
    }
});