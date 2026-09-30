
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const counter = document.getElementById("counter");
const message = document.getElementById("message");

let tasks = [];
let nextId = 1;

function updateCounter() {
    let completed = 0;
    let uncompleted = 0;

    for (const task of tasks) {
        if (task.completed) {
            completed++;
        } else {
            uncompleted++;
        }
    }

    counter.textContent =
        "Выполнено: " + completed +
        " | Не выполнено: " + uncompleted;
}

function renderTasks() {
    taskList.replaceChildren();

    for (const task of tasks) {
        const li = document.createElement("li");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.completed;

        const text = document.createElement("span");
        text.textContent = task.text;

        if (task.completed) {
            text.style.textDecoration = "line-through";
        }

        checkbox.addEventListener("change", function() {
            task.completed = checkbox.checked;
            renderTasks();
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Удалить";

        deleteButton.addEventListener("click", function() {
            tasks = tasks.filter(item => item.id !== task.id);
            renderTasks();
        });

        li.append(checkbox, text, deleteButton);
        taskList.append(li);
    }

    updateCounter();
}

document.getElementById("addTask").addEventListener("click", function() {
    const text = taskInput.value.trim();

    if (text === "") {
        message.textContent = "Введите название задачи!";
        return;
    }

    tasks.push({
        id: nextId++,
        text: text,
        completed: false
    });

    taskInput.value = "";
    message.textContent = "";

    renderTasks();
});

taskInput.addEventListener("input", function() {
    if (taskInput.value.trim() !== "") {
        message.textContent = "";
    }
});