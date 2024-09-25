from ninja import NinjaAPI, Schema
from ninja.orm import create_schema
from typing import List
from .models import NinjaTask

api = NinjaAPI()

# Create schemas
NinjaTaskSchema = create_schema(NinjaTask)

class NinjaTaskIn(Schema):
    title: str
    description: str = None
    priority: str = 'M'

@api.get("/tasks", response=List[NinjaTaskSchema])
def list_tasks(request):
    return NinjaTask.objects.all()

@api.post("/tasks", response=NinjaTaskSchema)
def create_task(request, task: NinjaTaskIn):
    task_dict = task.dict()
    return NinjaTask.objects.create(**task_dict)

@api.get("/tasks/{task_id}", response=NinjaTaskSchema)
def get_task(request, task_id: int):
    return NinjaTask.objects.get(id=task_id)

@api.put("/tasks/{task_id}", response=NinjaTaskSchema)
def update_task(request, task_id: int, data: NinjaTaskIn):
    task = NinjaTask.objects.get(id=task_id)
    for attr, value in data.dict().items():
        setattr(task, attr, value)
    task.save()
    return task

@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = NinjaTask.objects.get(id=task_id)
    task.delete()
    return {"success": True}

@api.put("/tasks/{task_id}/complete")
def complete_task(request, task_id: int):
    task = NinjaTask.objects.get(id=task_id)
    task.completed = True
    task.save()
    return {"success": True}