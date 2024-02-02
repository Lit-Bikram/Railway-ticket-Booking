from flask import Flask, render_template, request, redirect, url_for
import create_file as csvfile
from datetime import datetime
import q as q

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/meal.html")
def meal():
    return render_template("meal.html")

@app.route("/holiday.html")
def holiday():
    return render_template("holiday.html")

@app.route("/service.html")
def service():
    return render_template("service.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route('/getDetails', methods=['POST'])
def submit():
    if request.method == 'POST':
        source = request.form['from']
        to = request.form['to']
        date = request.form['date']
        bogie = request.form['bogie']
        person = request.form['person']
        
        print(source,to,date,bogie,person)
        return render_template("details.html",person = person)

@app.route('/submit', methods=['POST'])
def submit_details():
    global details
    person_value = int(request.form.get('person'))
    
    details = []
    for i in range(person_value):
        first_name = request.form.get(f'first-name-{i}')
        last_name = request.form.get(f'last-name-{i}')
        age = request.form.get(f'age-{i}')
        gender = request.form.get(f'gender-{i}')
        
        details.append({
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'gender': gender
        })
    
    csvfile.appendData(details)
    if len(details) == 1:
        q.singleAllocateSeat(details)
    else:
        q.multipleAllocateSeat(details)
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True,port=8000)