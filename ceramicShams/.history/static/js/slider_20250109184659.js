// $(".ModuleProduct1").owlCarousel({
//     loop: true,
//     margin: 30,
//     nav: true,
//     autoplayTimeout: 5000,
//     rtl: true,
//     autoplay: false,
//     autoWidth: true, // جلوگیری از تغییر عرض آیتم‌ها
//     responsive: {
//         0: {
//             items: 1
//         },
//         600: {
//             items: 3
//         },
//         1000: {
//             items: 5
//         }
//     },
//     onInitialized: function () {
//         console.log("Owl Carousel initialized");
//     }
// });

const swiper = new Swiper('.swiper-container', {
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    autoplay: {
      delay: 3000,
    },
  });
  
  