from .models import Task


def tasks(request):
    tasks = Task.objects.all()
    tasks = tasks.filter(assigned_to=request.user)
    tasks = tasks.filter(done=False)
    return {
        'my_active_tasks': tasks,
    }
