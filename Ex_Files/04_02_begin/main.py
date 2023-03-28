# pip install flask

from flask import Flask

app = Flask(__name__) #flask object

@app.route("/")
def hello():
    return "Hello, World!"

app.run(debug=True)