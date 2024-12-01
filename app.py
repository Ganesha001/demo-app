# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # In-memory data storage
# tasks = []

# @app.route('/')
# # def index():
# #     """Home route"""
# #     return "<h1>Welcome to the To-Do List API!</h1>"
# def index():
#     """Home route with a beautiful To-Do list interface"""
#     return render_template('index.html', tasks=tasks)

# @app.route('/add_task', methods=['POST'])
# def add_task():
#     """Add a new task to the list"""
#     task_data = request.json
#     task_name = task_data.get('task')
#     if not task_name:
#         return jsonify({'error': 'Task name is required'}), 400
    
#     task = {'id': len(tasks) + 1, 'task': task_name}
#     tasks.append(task)
#     return jsonify({'message': 'Task added successfully!', 'task': task}), 201

# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     """Retrieve all tasks"""
#     return jsonify({'tasks': tasks})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory data storage
tasks = []

@app.route('/')
def index():
    """Home route with a beautiful To-Do list interface"""
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task to the list"""
    task_data = request.json
    task_name = task_data.get('task')
    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400
    
    task = {'id': len(tasks) + 1, 'task': task_name, 'completed': False}
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!', 'task': task}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks"""
    return jsonify({'tasks': tasks})

@app.route('/mark_completed/<int:task_id>', methods=['POST'])
def mark_completed(task_id):
    """Mark a task as completed"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['completed'] = True
        return jsonify({'message': 'Task marked as completed!', 'task': task}), 200
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
