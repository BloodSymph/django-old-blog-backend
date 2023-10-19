// Set Listener
const setListener = (element, type, handler) => {
    if (element === null) {
        return;
    } else {
        element.addEventListener(type, handler);
    }
}

// Sliders
const headerSlide = document.querySelector('#header-hover__slider');
const homeSection = document.querySelector('.home-section');

setListener(headerSlide, 'click', () => {
    homeSection.scrollIntoView({
        behavior: "smooth",
        block: 'start',
    });
});

const aboutSlider = document.querySelector('#about-slider');
const skillSection = document.querySelector('.skills');

setListener(aboutSlider, 'click', (e) => {
    e.preventDefault();
    skillSection.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
    });
});

// Content Animation
function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('element-show');
        }
    });
}

let options = {
    threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');

for (let elm of elements) {
    observer.observe(elm);
}