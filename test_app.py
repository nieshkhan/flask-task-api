from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
   
def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"text": "belajar pytest"})
    assert response.status_code == 200
    assert response.get_json()["text"] == "belajar pytest"
    
def test_get_tasks():
    client = app.test_client()
    response = client.post("/tasks", json={"text": "belajar pytest"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert "tasks" in response.get_json()
    
def test_complete_task():
    client = app.test_client()
    client.post("/tasks", json={"text": "belajar pytest"})
    tasks_response = client.get("/tasks")
    last_index = len(tasks_response.get_json()["tasks"]) -1
    response = client.put(f"/tasks/{last_index}")
    assert response.status_code == 200
    assert response.get_json()["done"] == True
    
def test_delete_task():
    client = app.test_client()
    client.post("/tasks", json={"text": "belajar pytest"})
    tasks_response = client.get("/tasks")
    last_index = len(tasks_response.get_json()["tasks"]) -1
    response = client.delete(f"/tasks/{last_index}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Task berhasil dihapus"
    
    
    
