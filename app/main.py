from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="static")

todos = []

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Missing 'task'"}), 400
    todo = {"id": len(todos) + 1, "task": data["task"], "done": False}
    todos.append(todo)
    return jsonify(todo), 201

@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def mark_done(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            return jsonify(todo)
    return jsonify({"error": "Not found"}), 404

@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

