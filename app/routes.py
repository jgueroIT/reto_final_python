from flask import Blueprint, request, jsonify
from app import models

bp = Blueprint("routes", __name__)

@bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(models.get_all_tasks())

@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = models.get_task_by_id(task_id)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task_id = models.add_task(data["title"], data.get("description", ""))
    return jsonify({"id": task_id}), 201

@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    models.delete_task(task_id)
    return jsonify({"message": "Task deleted"})
