<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация аккаунта</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Регистрация аккаунта</h2>

        <form id="registrationForm">

            <label for="login">Логин:</label>
            <input type="text" id="login" placeholder="Введите логин">

            <label for="email">E-mail:</label>
            <input type="email" id="email" placeholder="Введите e-mail">

            <label for="password">Пароль:</label>
            <input type="password" id="password" placeholder="Введите пароль">

            <label for="confirmPassword">Повтор пароля:</label>
            <input type="password" id="confirmPassword" placeholder="Повторите пароль">

            <button type="submit">Зарегистрироваться</button>

            <p id="message"></p>

        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
