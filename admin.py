from flask import render_template,Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin.html")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True,port=4000)