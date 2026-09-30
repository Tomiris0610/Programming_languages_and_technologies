
const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const result = document.getElementById("result");

function calculate(operation) {
    if (num1.value === "" || num2.value === "") {
        result.textContent = "Введите оба числа!";
        return;
    }

    const a = Number(num1.value);
    const b = Number(num2.value);
    let answer;

    if (operation === "+") {
        answer = a + b;
    } else if (operation === "-") {
        answer = a - b;
    } else if (operation === "*") {
        answer = a * b;
    } else if (operation === "/") {
        if (b === 0) {
            result.textContent = "На ноль делить нельзя!";
            return;
        }
        answer = a / b;
    }

    result.textContent = "Результат: " + answer;
}

document.getElementById("add").addEventListener("click", () => {
    calculate("+");
});

document.getElementById("subtract").addEventListener("click", () => {
    calculate("-");
});

document.getElementById("multiply").addEventListener("click", () => {
    calculate("*");
});

document.getElementById("divide").addEventListener("click", () => {
    calculate("/");
});