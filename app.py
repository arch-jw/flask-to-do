from flask import Flask
from service import ToDoService
from models import Schema

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/<name>")
def hello_name(name):
    return "Hello, "+ name +"!"

@app.route("/todo", method=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

if __name__ == "__main__":
    app.run(debug=True)
