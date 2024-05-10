from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    current_date = timezone.now().date()  # Calculate the current date in the view
    return render(request, 'task_list.html', {'tasks': tasks, 'current_date': current_date})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def task_form(request, task_id=None):
    # If task_id is provided, get the corresponding task
    task = None
    if task_id:
        task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():  # Use `is_valid()` instead of `validate_on_submit()`
            form.save()
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm(instance=task)

    # Render the task form with the given form instance
    return render(request, 'task_form.html', {'form': form, 'task_id': task_id})


def task_delete(request, task_id):
    # Get the task to be deleted
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()  # Delete the task upon POST request
        return redirect('task_list')  # Redirect to the task list
    # Render a confirmation page for task deletion
    return render(request, 'task_confirm_delete.html', {'task': task})
