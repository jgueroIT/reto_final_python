import pytest
from app import models

def test_add_and_get_task():
    title = "Test Task"
    description = "Test Description"
    task_id = models.add_task(title, description)
    task = models.get_task_by_id(task_id)
    assert task['title'] == title
    assert task['description'] == description

def test_delete_task():
    title = "Task to Delete"
    description = "To be deleted"
    task_id = models.add_task(title, description)
    models.delete_task(task_id)
    task = models.get_task_by_id(task_id)
    assert task is None
