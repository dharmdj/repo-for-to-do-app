from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (replace with a persistent storage solution in a production environment)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    tasks.append({'content': task_content, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
