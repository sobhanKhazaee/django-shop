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
    loop: true, // فعال‌سازی حالت بی‌نهایت
    slidesPerView: 1, // فقط یک اسلاید در هر زمان
    slidesPerGroup: 1, // یک اسلاید در هر حرکت
    navigation: {
      nextEl: '.swiper-button-next', // دکمه بعدی
      prevEl: '.swiper-button-prev', // دکمه قبلی
    },
    pagination: {
      el: '.swiper-pagination', // صفحه‌بندی
      clickable: true, // کلیک‌پذیر
    },
    autoplay: {
      delay: 3000, // زمان‌بندی برای اتوپلی
      disableOnInteraction: false, // جلوگیری از توقف در تعامل
    },
    touchRatio: 1, // فعال کردن لمس
  });
  

