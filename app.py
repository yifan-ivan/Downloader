from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def download():
    print(request.form.get("input"))
    return render_template("index.html")

app.run(debug=True)