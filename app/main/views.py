from django.shortcuts import get_object_or_404, render
from main.models import Categories
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
    subcategories = category.get_subcategories()
    context = {
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'main/subcategories.html', context)