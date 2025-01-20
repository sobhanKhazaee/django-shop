const sliderContainer = document.getElementById("slider-container");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");

let currentSlide = 0;

// به‌روزرسانی موقعیت اسلایدر
function updateSlider() {
  const slideWidth = sliderContainer.parentElement.clientWidth; // عرض هر اسلاید
  sliderContainer.style.transform = `translateX(-${currentSlide * slideWidth}px)`; // حرکت به اسلاید مورد نظر
}

// حرکت به اسلاید بعدی
function goToNextSlide() {
  currentSlide = (currentSlide + 1) % sliderContainer.children.length; // اگر آخرین اسلاید بود به اول برمی‌گردد
  updateSlider();
}

// حرکت به اسلاید قبلی
function goToPrevSlide() {
  currentSlide = (currentSlide - 1 + sliderContainer.children.length) % sliderContainer.children.length; // اگر اولین اسلاید بود به آخر برمی‌گردد
  updateSlider();
}

// افزودن رویداد کلیک به دکمه‌ها
nextBtn.addEventListener("click", goToNextSlide);
prevBtn.addEventListener("click", goToPrevSlide);

// حرکت خودکار اسلایدر هر 2 ثانیه
let autoSlide = setInterval(goToNextSlide, 2000);

// توقف حرکت خودکار هنگام هاور روی اسلایدر
sliderContainer.addEventListener("mouseover", () => {
  clearInterval(autoSlide);
});

// شروع مجدد حرکت خودکار پس از خروج هاور
sliderContainer.addEventListener("mouseout", () => {
  autoSlide = setInterval(goToNextSlide, 2000);
});

// به‌روزرسانی اندازه اسلایدر هنگام تغییر اندازه صفحه
window.addEventListener("resize", updateSlider);

// مقداردهی اولیه
updateSlider();
