from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for homeworks
homeworks = []

@app.route('/')
def index():
    return render_template('index.html', homeworks=homeworks)

@app.route('/add', methods=['GET', 'POST'])
def add_homework():
    if request.method == 'POST':
        subject = request.form['subject']
        description = request.form['description']
        due_date = request.form['due_date']
        homeworks.append({
            'subject': subject,
            'description': description,
            'due_date': due_date
        })
        return redirect(url_for('index'))
    return render_template('add_homework.html')

@app.route('/delete/<int:homework_id>')
def delete_homework(homework_id):
    if 0 <= homework_id < len(homeworks):
        del homeworks[homework_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
