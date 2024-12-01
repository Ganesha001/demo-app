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
    
    task = {'id': len(tasks) + 1, 'task': task_name}
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!', 'task': task}), 201

@app.route('/delete_task', methods=['DELETE'])
def delete_task():
    """Delete a task"""
    task_data = request.json
    task_id = task_data.get('id')
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
