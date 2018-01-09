from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chronos.models import Category, Task
from chronos.forms import CategoryForm, TaskForm
from django.contrib.auth.decorators import login_required


def index(request):
    cat_pairs = None

    if request.user.is_authenticated:
        cats = list(Category.objects.filter(user=request.user))
        cat_pairs = list(zip(cats[::2], cats[1::2]))
        if len(cats) % 2:
            cat_pairs.append((cats[-1],))


    context_dict = {'cat_pairs': cat_pairs}

    return render(request, 'chronos/index.html', context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()

            return redirect('chronos:index')
        else:
            print(form.errors)

    return render(request, 'chronos/add_category.html', {'form': form})

@login_required
def add_task(request):
    task_name = request.POST.get('task_name')
    cat_id = request.POST.get('cat_id')[4:]

    if cat_id is None:
        return JsonResponse({'task_added': False})

    task = Task.objects.create(name=task_name, category=Category.objects.get(pk=int(cat_id)))

    data = {'task_added': True, 't_id': task.pk}

    return JsonResponse(data)

@login_required
def toggle_completion(request):
    t_id = request.POST.get('t_id')[4:]
    if t_id is None:
        return JsonResponse({})

    task = Task.objects.get(pk=int(t_id))
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()

    data = {'set_finished': task.is_finished}

    return JsonResponse(data)



@login_required
def remove_task(request):
    t_id = request.POST.get('t_id')[4:]
    if t_id is None:
        return JsonResponse({'task_removed': False})

    task = Task.objects.get(pk=int(t_id))
    task.delete()

    return JsonResponse({'task_removed': True})