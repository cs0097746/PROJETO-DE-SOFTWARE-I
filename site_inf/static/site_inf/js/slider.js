let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let dots = document.querySelectorAll('.slider .dots li');
let pauseButton = document.getElementById('pause');

let lengthItems = items.length - 1;
let active = 0;
let isPaused = false;

function nextSlide() {
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}

function reloadSlider() {
    slider.style.left = -items[active].offsetLeft + 'px';

    let last_active_dot = document.querySelector('.slider .dots li.active');
    if (last_active_dot) last_active_dot.classList.remove('active');
    dots[active].classList.add('active');
}

// Avanço automático
let refreshInterval = setInterval(nextSlide, 3000);

pauseButton.onclick = function () {
    const icon = pauseButton.querySelector('i');

    if (isPaused) {
        refreshInterval = setInterval(nextSlide, 3000);
        icon.classList.remove('fa-play');
        icon.classList.add('fa-pause');
    } else {
        clearInterval(refreshInterval);
        icon.classList.remove('fa-pause');
        icon.classList.add('fa-play');
    }

    isPaused = !isPaused;
};

// Clique nas bolinhas
dots.forEach((li, key) => {
    li.addEventListener('click', () => {
        active = key;
        reloadSlider();
    });
});

// Reajuste no resize
window.onresize = function () {
    reloadSlider();
};
