const ageInput = document.getElementById("age");

const result = document.getElementById("result");

document.getElementById("check").addEventListener("click", function() {

    const ageText = ageInput.value;

    if (ageText === "") {

        result.textContent = "Введите возраст!";

        return;

    }

    const age = Number(ageText);

    if (!Number.isInteger(age) || age < 0) {

        result.textContent = "Введите корректный возраст!";

    } else if (age < 13) {

        result.textContent = "Категория: ребёнок";

    } else if (age < 18) {

        result.textContent = "Категория: подросток";

    } else if (age < 60) {

        result.textContent = "Категория: взрослый";

    } else {

        result.textContent = "Категория: пожилой человек";

    }

});