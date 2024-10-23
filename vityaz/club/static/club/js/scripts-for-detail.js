document.addEventListener('DOMContentLoaded', function() {
    const customModal = document.getElementById('customModal');
    const closeModalButton = document.getElementById('closeModal');

    const sliders = {
        sbori: { buttonId: 'sboriButton', sliderId: 'sboriSlider', swiperInstance: null },
        sambo: { buttonId: 'samboButton', sliderId: 'samboSlider', swiperInstance: null },
        events: { buttonId: 'eventsButton', sliderId: 'eventsSlider', swiperInstance: null },
        karate: { buttonId: 'karateDetailsButton', sliderId: 'karateSlider', swiperInstance: null },
        techvando: { buttonId: 'techvandoDetailsButton', sliderId: 'techvandoSlider', swiperInstance: null }
    };

    function openModal(type) {
        customModal.style.display = "block";
        hideAllSliders();

        const sliderInfo = sliders[type];
        if (!sliderInfo) {
            return;
        }

        const sliderElement = document.getElementById(sliderInfo.sliderId);
        if (!sliderElement) {
            return;
        }

        sliderElement.style.display = 'block';

        if (!sliderInfo.swiperInstance) {
            sliderInfo.swiperInstance = initSwiper(`#${sliderInfo.sliderId}`);
        } else {
            sliderInfo.swiperInstance.update();
        }
    }

    function hideAllSliders() {
        Object.values(sliders).forEach(({ sliderId }) => {
            const elem = document.getElementById(sliderId);
            if (elem) {
                elem.style.display = 'none';
            }
        });
    }

    function closeModal() {
        customModal.style.display = "none";
        hideAllSliders();
    }

    Object.entries(sliders).forEach(([type, { buttonId }]) => {
        const buttonElement = document.getElementById(buttonId);
        if (buttonElement) {
            buttonElement.addEventListener('click', () => openModal(type));
        }
    });

    if (closeModalButton) {
        closeModalButton.addEventListener('click', closeModal);
    }

    window.onclick = function(event) {
        if (event.target === customModal) {
            closeModal();
        }
    }

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
