
document.addEventListener('DOMContentLoaded', function() {
// Получение всех элементов кнопок
const sboriButton = document.getElementById('sboriButton');
const samboButton = document.getElementById('samboButton');
const eventsButton = document.getElementById('eventsButton');
const karateDetailsButton = document.getElementById('karateDetailsButton');
const techvandoDetailsButton = document.getElementById('techvandoDetailsButton');
const closeModalButton = document.getElementById('closeModal');
const customModal = document.getElementById('customModal');

// Переменные для хранения экземпляров Swiper
let sboriSwiper, eventsSwiper, karateSwiper, techvandoSwiper, samboSwiper;

// Добавление обработчиков событий для кнопок
if (sboriButton) {
    sboriButton.addEventListener('click', function() {
        openModal('sbori');
    });
}
if (samboButton) {
    samboButton.addEventListener('click', function() {
        openModal('sambo');
    });
}

if (eventsButton) {
    eventsButton.addEventListener('click', function() {
        openModal('events');
    });
}

if (karateDetailsButton) {
    karateDetailsButton.addEventListener('click', function() {
        openModal('karate');
    });
}

if (techvandoDetailsButton) {
    techvandoDetailsButton.addEventListener('click', function() {
        openModal('techvando');
    });
}

if (closeModalButton) {
    closeModalButton.addEventListener('click', closeModal);
}

// Функция открытия модального окна
function openModal(type) {
    customModal.style.display = "block";
    hideAllSliders();

    switch (type) {
        case 'sbori':
            document.getElementById('sboriSlider').style.display = 'block';
            if (!sboriSwiper) {
                sboriSwiper = initSwiper('#sboriSlider');
            }
            break;
        case 'sambo':
            document.getElementById('samboSlider').style.display = 'block';
            if (!samboSwiper) {
                samboSwiper = initSwiper('#samboSlider');
            }
            break;
        case 'events':
            document.getElementById('eventsSlider').style.display = 'block';
            if (!eventsSwiper) {
                eventsSwiper = initSwiper('#eventsSlider');
            }
            break;
        case 'karate':
            document.getElementById('karateSlider').style.display = 'block';
            if (!karateSwiper) {
                karateSwiper = initSwiper('#karateSlider');
            }
            break;
        case 'techvando':
            document.getElementById('techvandoSlider').style.display = 'block';
            if (!techvandoSwiper) {
                techvandoSwiper = initSwiper('#techvandoSlider');
            }
            break;
    }
}

// Функция скрытия всех слайдеров
function hideAllSliders() {
    document.getElementById('sboriSlider').style.display = 'none';
    document.getElementById('samboSlider').style.display = 'none';
    document.getElementById('eventsSlider').style.display = 'none';
    document.getElementById('karateSlider').style.display = 'none';
    document.getElementById('techvandoSlider').style.display = 'none';
}

// Функция закрытия модального окна
function closeModal() {
    customModal.style.display = "none";
    hideAllSliders();
}
// Закрытие модального окна при нажатии на затемнённую область
window.onclick = function(event) {
    if (event.target === customModal) {
        closeModal();
    }
}

// Функция инициализации Swiper
function initSwiper(selector) {
    return new Swiper(selector, {
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        slidesPerView: 1,
        spaceBetween: 30,
        speed: 600,
    });
}
});