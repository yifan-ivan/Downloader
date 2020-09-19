from flask import Flask, render_template, request, send_file
# from you_get import common
import os
import zipfile

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def download():
    hello = "sdads"
    user_input = request.form.get("input")

    print(type(user_input))

    check = user_input.lower()

    # Check input
    if check.startswith("av") or check.startswith("bv"):
        user_input = f'"http://www.bilibili.com/video/{user_input}"'

    cmd = f"you-get {user_input} -O video"

    print(f"Downloading {user_input}...")
    
    os.system(cmd)

    # os.remove("video.webm")

    return render_template("index.html")

    # return send_file("video.webm", as_attachment=True)

    # return send_file("test.zip", as_attachment=True)

app.run(debug=True, host="0.0.0.0", port="80")