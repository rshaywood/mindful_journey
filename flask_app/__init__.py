from flask import Flask
app = Flask(__name__)
app.secret_key = "success"
app.config["UPLOAD_FOLDER"]="flask_app/static/images" #this path for uploading image from local computer and save it in app.config to use it later in our controller




