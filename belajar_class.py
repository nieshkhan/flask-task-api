import json

class Task:
    def __init__(self, text):
        self.text = text
        self.done = False
    
    def mark_done(self):
        self.done = True
        
    def to_dict(self):
        return {"text": self.text, "done": self.done}
        
task1 = Task("Belajar Python")
task2 = Task("Belajar Flask") 

tasks = [task1, task2]

def save_tasks():
    tasks_as_dict = []
    for task in tasks:
        tasks_as_dict.append(task.to_dict())
    with open("tasks.json", "w") as f:
        json.dump(tasks_as_dict, f)

save_tasks()

task1.mark_done()

print(task1.to_dict())
print(task1.text)
print(task2.text)
print(task1.done)
print(task2.done)