const sliderContainer = document.getElementById('slider-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

let currentIndex = 0;

const updateSlider = () => {
    sliderContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
};

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : 0;
    updateSlider();
});

nextBtn.addEventListener('click', () => {
    const items = sliderContainer.children.length;
    currentIndex = (currentIndex < items - 1) ? currentIndex + 1 : items - 1;
    updateSlider();
});
