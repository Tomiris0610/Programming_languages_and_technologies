<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Регистрация студента</title>
</head>
<body>

<h2>Форма регистрации студента</h2>

<form id="studentForm">

    <label for="fullName">ФИО:</label>
    <input id="fullName" type="text" placeholder="Введите ФИО">
    <br><br>

    <label for="email">E-mail:</label>
    <input id="email" type="email" placeholder="Введите e-mail">
    <br><br>

    <label for="course">Курс:</label>
    <select id="course">
        <option value="">Выберите курс</option>
        <option value="1">1 курс</option>
        <option value="2">2 курс</option>
        <option value="3">3 курс</option>
        <option value="4">4 курс</option>
    </select>
    <br><br>

    <label>
        <input id="agree" type="checkbox">
        Согласен с правилами
    </label>
    <br><br>

    <button type="submit">Зарегистрироваться</button>

</form>

<p id="message"></p>

<script>
    const form = document.getElementById('studentForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const fullName = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const course = document.getElementById('course').value;
        const agree = document.getElementById('agree').checked;
        const message = document.getElementById('message');

        if (fullName === '') {
            message.textContent = 'Введите ФИО';
            return;
        }

        if (email === '') {
            message.textContent = 'Введите e-mail';
            return;
        }

        if (course === '') {
            message.textContent = 'Выберите курс';
            return;
        }

        if (!agree) {
            message.textContent = 'Подтвердите согласие с правилами';
            return;
        }

        message.textContent = 'Форма заполнена корректно. Регистрация выполнена!';
    });
</script>

</body>
</html>
