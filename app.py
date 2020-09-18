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
    url = request.form.get("input")
    cmd = f"you-get {url} -o tmp -O video"

    print("Downloading ...")

    # r = os.popen(cmd)  
    # text = r.read()  
    # r.close()  
    # print("Got those: \n" + text)
    
    os.system(cmd)

    # return render_template("index.html")

    f = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
    f.write("tmp/video.webm")
    f.close()

    return send_file("test.zip", as_attachment=True)

app.run(debug=True)