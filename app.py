import json
from flask import Flask, request
app = Flask(__name__)

tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
        
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
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
    new_task = {"text": data["text"], "done": False}
    tasks.append(new_task)
    save_tasks()
    return new_task
    
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return {"tasks": tasks}


@app.route("/tasks/<int:index>", methods=["PUT"])
def complete_task(index):
    if index < 0 or index >= len(tasks):
        return {"error": "Task tidak ditemukan"}, 404
    tasks[index]["done"] = True
    save_tasks()
    return tasks[index]


@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < 0 or index >= len(tasks):
        return {"error": "Task tidak ditemukan"}, 404
    del tasks[index]
    save_tasks()
    return {"message": "Task berhasil dihapus"}
    

if __name__ == "__main__":
    app.run(debug=True)
