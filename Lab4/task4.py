```html
<form id="profileForm">

  <input id="name" type="text" placeholder="Имя">

  <input id="age" type="number" placeholder="Возраст">

  <select id="language">
    <option value="">Выберите язык интерфейса</option>
    <option value="Русский">Русский</option>
    <option value="Казахский">Казахский</option>
    <option value="Английский">Английский</option>
  </select>

  <p>Выберите интересы:</p>

  <label>
    <input type="checkbox" name="interest" value="Музыка">
    Музыка
  </label>

  <label>
    <input type="checkbox" name="interest" value="Спорт">
    Спорт
  </label>

  <label>
    <input type="checkbox" name="interest" value="Игры">
    Игры
  </label>

  <label>
    <input type="checkbox" name="interest" value="Путешествия">
    Путешествия
  </label>

  <button type="submit">Создать профиль</button>

</form>

<p id="message"></p>

<div id="profileCard"></div>

<script>

const form = document.getElementById('profileForm');

form.addEventListener('submit', function(event) {

  event.preventDefault();

  const name = document.getElementById('name').value.trim();
  const age = document.getElementById('age').value;
  const language = document.getElementById('language').value;

  const interests = document.querySelectorAll(
    'input[name="interest"]:checked'
  );

  const message = document.getElementById('message');
  const profileCard = document.getElementById('profileCard');

  if (name === '') {
    message.textContent = 'Введите имя';
    return;
  }

  if (age === '' || age < 1 || age > 120) {
    message.textContent = 'Введите корректный возраст';
    return;
  }

  if (language === '') {
    message.textContent = 'Выберите язык интерфейса';
    return;
  }

  if (interests.length === 0) {
    message.textContent = 'Выберите хотя бы один интерес';
    return;
  }

  const interestsList = [];

  interests.forEach(function(interest) {
    interestsList.push(interest.value);
  });

  message.textContent = 'Профиль создан';

  profileCard.innerHTML =
    '<h3>Карточка профиля</h3>' +
    '<p>Имя: ' + name + '</p>' +
    '<p>Возраст: ' + age + '</p>' +
    '<p>Язык интерфейса: ' + language + '</p>' +
    '<p>Интересы: ' + interestsList.join(', ') + '</p>';

});

</script>
```
