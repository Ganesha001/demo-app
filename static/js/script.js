// Add a new task
function addTask() {
    const taskName = document.getElementById("task-name").value;
    if (taskName) {
        // Send the task to the backend (you can modify this to interact with the server)
        const task = {
            task: taskName
        };

        fetch('/add_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(task)
        })
        .then(response => response.json())
        .then(data => {
            const task = data.task;
            const taskList = document.getElementById('task-list');
            const newTask = document.createElement('li');
            newTask.className = 'task-item';
            newTask.id = 'task-' + task.id;
            newTask.innerHTML = `
                <input type="checkbox" id="checkbox-${task.id}" onclick="toggleTask(${task.id})">
                <span class="task-text">${task.task}</span>
                <button class="delete-btn" onclick="deleteTask(${task.id})">❌</button>
            `;
            taskList.appendChild(newTask);
            newTask.classList.add('task-added');
            document.getElementById("task-name").value = '';  // Reset the input field
        })
        .catch(error => console.error('Error adding task:', error));
    }
}

// Toggle task completion
function toggleTask(taskId) {
    const taskItem = document.getElementBy
