import json
from flask import Flask, request
app = Flask(__name__)

class Task:
    
    def __init__(self, text):
        self.text = text
        self.done = False
        
    def mark_done(self):
        self.done = True
        
    def to_dict(self):
        return {"text": self.text, "done": self.done}
        
tasks = []

def save_tasks():
    tasks_as_dict = []
    for task in tasks:
        tasks_as_dict.append(task.to_dict())
    with open("tasks.json", "w") as f:
        json.dump(tasks_as_dict, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            loaded_data = json.load(f)
        
        tasks = []
                    
        for item in loaded_data:
            new_task = Task(item["text"])
            if item["done"] == True:
                new_task.mark_done()
            tasks.append(new_task)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
load_tasks()

@app.route("/")
def home():
    return "Hello, ini API pertama saya!"
    

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if data is None or "text" not in data or not data["text"] or not isinstance(data["text"], str):
        return {"error": "Data tidak valid"}, 400
    new_task =  Task(data["text"])
    tasks.append(new_task)
    save_tasks()
    return new_task.to_dict(), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks_as_dict = []
    for task in tasks:
        tasks_as_dict.append(task.to_dict())
    return {"tasks": tasks_as_dict}


@app.route("/tasks/<int:index>", methods=["PUT"])
def complete_task(index):
    if index < 0 or index >= len(tasks):
        return {"error": "Task tidak ditemukan"}, 404
    tasks[index].mark_done()
    save_tasks()
    return tasks[index].to_dict()


@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < 0 or index >= len(tasks):
        return {"error": "Task tidak ditemukan"}, 404
    del tasks[index]
    save_tasks()
    return {"message": "Task berhasil dihapus"}
    

if __name__ == "__main__":
    app.run(debug=True)
