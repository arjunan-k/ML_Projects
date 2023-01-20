// Define UI Vars
const form = document.querySelector('#task-form');
const taskList = document.querySelector('.collection');
const clear = document.querySelector('.clear-tasks');
const filter = document.querySelector('#filter');
const taskInput = document.querySelector('#task');

// Load all event listeners
loadEventListener();

function loadEventListener() {
    form.addEventListener('submit', addTask);
}

function addTask(e) {
    if(taskInput.value === "") {
        alert('Add a task')
    }

    const li = document.createElement('li');
    li.className = 'collection-item'
    li.appendChild(document.createTextNode(taskInput.value))
    const link = document.createElement('a');
    link.className = 'delete-item secondary-content';
    link.innerHTML = '<i class="fa fa-remove"></li>';
    // link.textContent = '<i class="fa fa-remove"></li>';
    li.appendChild(link);
    taskList.appendChild(li)
    taskInput.value = ""
    console.log(li)
    e.preventDefault();
}