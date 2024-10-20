// Функция открытия формы
function openForm(type) {
    document.getElementById("overlay").style.display = "block";
    if (type === 'trial') {
        document.getElementById("trial-form-popup").style.display = "block";
        document.getElementById("trial-form-popup").classList.add("visible");
    } else if (type === 'callback') {
        document.getElementById("callback-form-popup").style.display = "block";
        document.getElementById("callback-form-popup").classList.add("visible");
    }
}

// Функция закрытия формы
function closeForm() {
    document.getElementById("overlay").style.display = "none";
    var trialForm = document.getElementById("trial-form-popup");
    var callbackForm = document.getElementById("callback-form-popup");
    if (trialForm) {
        trialForm.style.display = "none";
        trialForm.classList.remove("visible");
    }
    if (callbackForm) {
        callbackForm.style.display = "none";
        callbackForm.classList.remove("visible");
    }
}

// При загрузке документа, открываем форму если была ошибка
document.addEventListener("DOMContentLoaded", function() {
    var visibleForm = document.querySelector('.form-popup.visible');
    if (visibleForm) {
        visibleForm.style.display = 'block';
        document.getElementById("overlay").style.display = "block";
    }
});

// Callback функция для reCAPTCHA
function onRecaptchaSuccess(token) {
    console.log("reCAPTCHA успешно пройдена");
    var visibleForm = document.querySelector('.form-popup.visible');
    if (visibleForm) {
        var submitButton = visibleForm.querySelector('.btn');
        if (submitButton) {
            console.log("Разблокируем кнопку отправки");
            submitButton.disabled = false;
        } else {
            console.error("Кнопка отправки не найдена");
        }
    } else {
        console.error("Открытая форма не найдена");
    }
    }


// Проверяем, существует ли элемент с классом success-message
document.addEventListener("DOMContentLoaded", function() {
    var successMessage = document.querySelector('.success-message');
    if (successMessage) {
        // Устанавливаем таймер на 5 секунд для начала анимации исчезновения
        setTimeout(function() {
            successMessage.classList.add('fade-out');
        }, 5000);
    }
});