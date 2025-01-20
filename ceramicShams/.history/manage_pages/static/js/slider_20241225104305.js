const sliderContainer = document.getElementById("slider-container");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");

let currentSlide = 0;

function updateSlider() {
  const slideWidth = sliderContainer.clientWidth;
  sliderContainer.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}

nextBtn.addEventListener("click", () => {
  currentSlide = (currentSlide + 1) % sliderContainer.children.length;
  updateSlider();
});

prevBtn.addEventListener("click", () => {
  currentSlide = (currentSlide - 1 + sliderContainer.children.length) % sliderContainer.children.length;
  updateSlider();
});

window.addEventListener("resize", updateSlider);
