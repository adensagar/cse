from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    urn = request.form["urn"]
    file = request.files["file"]

    folder_path = os.path.join(UPLOAD_FOLDER, urn)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file.save(os.path.join(folder_path, file.filename))

    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)