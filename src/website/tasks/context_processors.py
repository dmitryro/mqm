from .models import Task


def tasks(request):
    if request.user.is_authenticated():
        tasks = request.user.tasks.all()
        tasks = tasks.filter(done=False)
        return {
            'my_active_tasks': tasks,
        }
    return {}
