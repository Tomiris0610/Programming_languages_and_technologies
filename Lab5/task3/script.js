
const nameInput = document.getElementById("name");
const groupInput = document.getElementById("group");
const courseInput = document.getElementById("course");
const card = document.getElementById("card");
const message = document.getElementById("message");

function createCard(name, group, course) {
    const studentCard = document.createElement("div");

    studentCard.style.border = "2px solid blue";
    studentCard.style.padding = "15px";
    studentCard.style.marginTop = "15px";
    studentCard.style.width = "250px";

    const title = document.createElement("h2");
    title.textContent = name;

    const groupInfo = document.createElement("p");
    groupInfo.textContent = "Группа: " + group;

    const courseInfo = document.createElement("p");
    courseInfo.textContent = "Курс: " + course;

    studentCard.append(title, groupInfo, courseInfo);

    return studentCard;
}

document.getElementById("create").addEventListener("click", function() {
    const name = nameInput.value.trim();
    const group = groupInput.value.trim();
    const courseText = courseInput.value.trim();
    const course = Number(courseText);

    if (name === "" || group === "" || courseText === "") {
        message.textContent = "Заполните все поля!";
        card.replaceChildren();
    } else if (!Number.isInteger(course) || course < 1 || course > 6) {
        message.textContent = "Введите курс от 1 до 6!";
        card.replaceChildren();
    } else {
        message.textContent = "";
        card.replaceChildren(createCard(name, group, course));
    }
});