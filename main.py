from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# In-memory task storage using a dictionary
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

def validate_input(input_text):
    allowed_chars = r"^[^#]+$"  # Disallow # symbol
    if re.match(allowed_chars, input_text):
        return input_text
    return None

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        sanitized_task = validate_input(task)
        if sanitized_task:
            tasks[sanitized_task] = "Pending"
    return redirect(url_for('index'))

@app.route('/delete/<task>', methods=['POST'])
def delete_task(task):
    if task in tasks:
        del tasks[task]
    return redirect(url_for('index'))

@app.route('/toggle/<task>', methods=['POST'])
def toggle_task_status(task):
    if task in tasks:
        tasks[task] = "Done" if tasks[task] == "Pending" else "Pending"
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
