from django.shortcuts import redirect, render, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdatedForm

# Create your views here.


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, "todo/list.html", context)


def todo_add(request):
    form = TodoAddForm()
    if(request.method == 'POST'):
        form = TodoAddForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("list")

    context = {
        'form': form,
    }

    return render(request, "todo/add.html", context)


def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdatedForm(instance=todo)

    if request.method == 'POST':
        form = TodoUpdatedForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        'form': form,
    }

    return render(request, "todo/updated.html", context)


def todo_delete(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)


    if request.method == 'POST':
        todo.delete()
        return redirect("list")

    context = {
        'todo': todo,
    }

    return render(request, "todo/delete.html", context)
