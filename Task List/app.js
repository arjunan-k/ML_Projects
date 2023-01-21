// Define UI Vars
const form = document.querySelector('#task-form');
const taskList = document.querySelector('.collection');
const clearBtn = document.querySelector('.clear-tasks');
const filter = document.querySelector('#filter');
const taskInput = document.querySelector('#task');

// Load all event listeners
loadEventListener();

function loadEventListener() {
    document.addEventListener('DOMContentLoaded', getTasks)
    form.addEventListener('submit', addTask);
    taskList.addEventListener('click', delTask)
    clearBtn.addEventListener('click', removeTask);
    filter.addEventListener('keyup', filterTask);
}

function addTask(e) {
    if(taskInput.value === "") {
        alert('Add a task');
        e.preventDefault();
        return;
    }

    const li = document.createElement('li');
    li.className = 'collection-item'
    li.appendChild(document.createTextNode(taskInput.value))
    const link = document.createElement('a');
    link.className = 'delete-item secondary-content';
    link.innerHTML = '<i class="fa fa-remove"></i>';
    // link.textContent = '<i class="fa fa-remove"></i>';
    li.appendChild(link);
    taskList.appendChild(li)
    storeTaskInLocalStorage(taskInput.value);
    taskInput.value = ""
    // console.log(li)
    e.preventDefault();
}

function delTask(e){
    if (e.target.parentElement.classList.contains('delete-item')) {
        if (confirm('Are you sure?')) {
            e.target.parentElement.parentElement.remove();

            removeTaskFromLocalStorage(e.target.parentElement.parentElement)
        }
    };
}

function removeTask(e) {
    // taskList.innerHTML = ""
    if(confirm('Are you sure?')) {
    while(taskList.firstChild){
        taskList.removeChild(taskList.firstChild)
    }

    clearTaskFromLocalStorage();
}
}

function filterTask(e){
    const text = e.target.value.toLowerCase();
    // console.log(text);
    document.querySelectorAll('.collection-item').forEach(
        function(task){
            const item = task.firstChild.textContent;
            if(item.toLowerCase().indexOf(text) != -1) {
                task.style.display = 'block';
            } else {
                task.style.display = 'none';
            }
        }
    );
}

function storeTaskInLocalStorage(task){
    let tasks;
    if (localStorage.getItem('tasks') === null){
        tasks = []
    } else{
        tasks = JSON.parse(localStorage.getItem('tasks'))
    }
    tasks.push(task)
    localStorage.setItem('tasks', JSON.stringify(tasks))
}

function getTasks(){
    let tasks;
    if (localStorage.getItem('tasks') === null){
        tasks = []
    } else{
        tasks = JSON.parse(localStorage.getItem('tasks'))
    }

    tasks.forEach(function(task){
        const li = document.createElement('li');
        li.className = 'collection-item'
        li.appendChild(document.createTextNode(task))
        const link = document.createElement('a');
        link.className = 'delete-item secondary-content';
        link.innerHTML = '<i class="fa fa-remove"></i>';
        // link.textContent = '<i class="fa fa-remove"></i>';
        li.appendChild(link);
        taskList.appendChild(li)
    })
}

function removeTaskFromLocalStorage(taskItem) {
    let tasks;
    if (localStorage.getItem('tasks') === null){
        tasks = []
    } else{
        tasks = JSON.parse(localStorage.getItem('tasks'))
    }

    tasks.forEach(function(task, index) {
        if(taskItem.textContent === task) {
            tasks.splice(index, 1)
        }
    });

    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function clearTaskFromLocalStorage(){
    localStorage.clear();
}