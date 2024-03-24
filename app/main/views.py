from django.shortcuts import get_object_or_404, redirect, render
from main.models import Categories,PostTasks
# Create your views here.

def index(request):
    categories = Categories.objects.all()

    context = {
        'categories': categories,
        'title': 'Уроки інформатики',
    }
    return render(request, 'main/index.html', context)


def subcategories(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    categories = category.get_subcategories()
    tasks = PostTasks.objects.filter(category__slug=category_slug)
    if tasks:

        context = {
            'tasks': tasks,
        }
        return render(request, 'main/all_tasks.html', context)
    else:  
        context = {
            'category': category,
            'categories': categories,
        }
        return render(request,'main/subcategories.html', context)
        

def show_all_tasks(request):
    tasks = PostTasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'main/all_tasks.html', context)
    