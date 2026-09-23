```html
<form id="internshipForm">

  <input id="fullname" type="text" placeholder="ФИО">

  <input id="email" type="email" placeholder="E-mail">

  <select id="course">
    <option value="">Выберите курс</option>
    <option value="1">1 курс</option>
    <option value="2">2 курс</option>
    <option value="3">3 курс</option>
    <option value="4">4 курс</option>
  </select>

  <select id="direction">
    <option value="">Выберите направление</option>
    <option value="Программирование">Программирование</option>
    <option value="Дизайн">Дизайн</option>
    <option value="Тестирование">Тестирование</option>
    <option value="Аналитика">Аналитика</option>
  </select>

  <p>Навыки:</p>

  <label>
    <input type="checkbox" name="skill" value="HTML/CSS">
    HTML/CSS
  </label>

  <label>
    <input type="checkbox" name="skill" value="JavaScript">
    JavaScript
  </label>

  <label>
    <input type="checkbox" name="skill" value="Python">
    Python
  </label>

  <label>
    <input type="checkbox" name="skill" value="SQL">
    SQL
  </label>

  <textarea id="motivation" placeholder="Мотивационный текст"></textarea>

  <button type="submit">Отправить заявку</button>

</form>

<p id="message"></p>

<script>

const form = document.getElementById('internshipForm');

form.addEventListener('submit', function(event) {

  event.preventDefault();

  const fullname = document.getElementById('fullname').value.trim();
  const email = document.getElementById('email').value.trim();
  const course = document.getElementById('course').value;
  const direction = document.getElementById('direction').value;
  const motivation = document.getElementById('motivation').value.trim();

  const skills = document.querySelectorAll(
    'input[name="skill"]:checked'
  );

  const message = document.getElementById('message');

  if (fullname === '') {
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

  if (direction === '') {
    message.textContent = 'Выберите направление';
    return;
  }

  if (skills.length < 2) {
    message.textContent = 'Выберите минимум два навыка';
    return;
  }

  if (motivation.length < 50) {
    message.textContent = 'Мотивационный текст должен содержать минимум 50 символов';
    return;
  }

  message.textContent = 'Заявка успешно отправлена';

});

</script>
```
