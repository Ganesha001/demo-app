from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
tasks = []

@app.route('/')
def index():
    """Home route"""
    return "<h1>Welcome to the To-Do List API!</h1>"

@app.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task to the list"""
    task_data = request.json
    task_name = task_data.get('task')
    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400
    
    task = {'id': len(tasks) + 1, 'task': task_name}
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!', 'task': task}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks"""
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
