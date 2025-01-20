const sliderContainer = document.getElementById('slider-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

let currentIndex = 0;
const items = sliderContainer.children.length;
const itemsPerView = 4; // Number of items visible in one view
const totalSlides = Math.ceil(items / itemsPerView);

const updateSlider = () => {
    sliderContainer.style.transform = `translateX(-${currentIndex * (100 / itemsPerView)}%)`;
};

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalSlides - 1;
    updateSlider();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex < totalSlides - 1) ? currentIndex + 1 : 0;
    updateSlider();
});


