from ninja import Router, Schema
from typing import List
from .models import NinjaTask

router = Router()

class TaskSchema(Schema):
    id: int
    title: str
    description: str = None
    completed: bool

class TaskIn(Schema):
    title: str
    description: str = None

@router.get("/tasks", response=List[TaskSchema])
def list_tasks(request):
    return list(NinjaTask.objects.all())

@router.post("/tasks", response=TaskSchema)
def create_task(request, task: TaskIn):
    return NinjaTask.objects.create(**task.dict())

@router.get("/tasks/{task_id}", response=TaskSchema)
def get_task(request, task_id: int):
    return NinjaTask.objects.get(id=task_id)

@router.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, data: TaskIn):
    task = NinjaTask.objects.get(id=task_id)
    for attr, value in data.dict().items():
        setattr(task, attr, value)
    task.save()
    return task

@router.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = NinjaTask.objects.get(id=task_id)
    task.delete()
    return {"success": True}