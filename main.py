from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage using a dictionary
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks.keys())  # Get all task names from the dictionary

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks[task] = "Pending"  # Store task in the dictionary
    return redirect(url_for('index'))

@app.route('/delete/<task>', methods=['POST'])
def delete_task(task):
    if task in tasks:
        del tasks[task]  # Remove task from the dictionary
    return redirect(url_for('index'))

@app.route('/complete/<task>', methods=['POST'])
def complete_task(task):
    if task in tasks and tasks[task] == "Pending":
        tasks[task] = "Done"  # Mark task as done
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)