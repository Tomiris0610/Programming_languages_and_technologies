<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Регистрация аккаунта</title>
</head>
<body>

<h2>Регистрация аккаунта</h2>

<form id="registrationForm">

    <label for="login">Логин:</label>
    <input id="login" type="text" placeholder="Введите логин">
    <br><br>

    <label for="email">E-mail:</label>
    <input id="email" type="email" placeholder="Введите e-mail">
    <br><br>

    <label for="password">Пароль:</label>
    <input id="password" type="password" placeholder="Введите пароль">
    <br><br>

    <label for="confirmPassword">Повторите пароль:</label>
    <input id="confirmPassword" type="password" placeholder="Повторите пароль">
    <br><br>

    <button type="submit">Зарегистрироваться</button>

</form>

<p id="message"></p>

<script>
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const login = document.getElementById('login').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const message = document.getElementById('message');

        if (login === '') {
            message.textContent = 'Введите логин';
            return;
        }

        if (email === '') {
            message.textContent = 'Введите e-mail';
            return;
        }

        if (password === '') {
            message.textContent = 'Введите пароль';
            return;
        }

        if (password.length < 8) {
            message.textContent = 'Пароль должен содержать не менее 8 символов';
            return;
        }

        if (confirmPassword === '') {
            message.textContent = 'Повторите пароль';
            return;
        }

        if (password !== confirmPassword) {
            message.textContent = 'Пароли не совпадают';
            return;
        }

        message.textContent = 'Регистрация выполнена успешно!';
    });
</script>

</body>
</html>
