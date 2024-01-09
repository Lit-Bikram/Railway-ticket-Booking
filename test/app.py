from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['dates']
        department = request.form['department']
        return f"Submitted: Name - {name}, Email - {email}, Date - {date}, department - {department}"

if __name__ == '__main__':
    app.run(debug=True)
