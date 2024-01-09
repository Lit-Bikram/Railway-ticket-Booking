from flask import Flask,render_template, request

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

if __name__ == "__main__":
    app.run(debug=True,port=8000)