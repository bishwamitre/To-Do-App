from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task storage using a dictionary
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)  # Pass the dictionary of tasks

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks[task] = "Pending"  # Add task with 'Pending' status
    return redirect(url_for('index'))

@app.route('/delete/<task>', methods=['POST'])
def delete_task(task):
    if task in tasks:
        del tasks[task]  # Delete task from the dictionary
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
