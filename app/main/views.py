from django.shortcuts import get_object_or_404, render
from main.models import Categories,PostTasks,Post,PinnedPost
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
    categories2 = Categories.objects.filter(parent_category=category)
    tasks = PostTasks.objects.filter(category__slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
   

       # Отримуємо всі підкатегорії включаючи основну категорію
    all_categories = [category] + list(categories2)
    
    # Отримуємо всі пости для усіх категорій
    all_posts   = Post.objects.filter(category__in=all_categories)
    
    # Отримуємо всі закріплені пости для усіх категорій
    pinned_posts = PinnedPost.objects.filter(category__in=all_categories)
    # pinned_posts = []
    # for subcategory in categories:
    #     pinned_posts.extend(Post.objects.filter(category=subcategory, is_favorite=True))  # Отримуємо всі закріплені пости для кожної підкатегорії і додаємо їх до загального списку
    # 
    if tasks:

        context = {
            'tasks': tasks,
        }
        return render(request, 'main/all_tasks.html', context)
    elif posts and category:
        context = {
            'posts': posts,
            'category': category,
            'categories': categories,
            'pinned_posts': pinned_posts,
        }
        return render(request,'main/subcategories.html', context)
    elif posts :
        context = {
            'posts': posts,
            'pinned_posts': pinned_posts,
        }
        return render(request,'main/subcategories.html', context) 
    else:  
        context = {
            'category': category,
            'categories': categories,
            'pinned_posts': pinned_posts,
            
        }
        return render(request,'main/subcategories.html', context)

# def subcategories(request, category_slug):
#     category = get_object_or_404(Categories, slug=category_slug)

#     # Отримуємо всі підкатегорії для основної категорії
#     categories = Categories.objects.filter(parent_category=category)

#     # Отримуємо всі пости для поточної категорії (не включаючи пости з підкатегорій)
#     current_category_posts = Post.objects.filter(category=category)

#     # Отримуємо всі пости для усіх підкатегорій
#     subcategories_posts = Post.objects.filter(category__in=categories)

#     # Об'єднуємо пости для поточної категорії та її підкатегорій
#     all_posts = current_category_posts | subcategories_posts

#     # Отримуємо всі закріплені пости для поточної категорії та її підкатегорій
#     pinned_posts = PinnedPost.objects.filter(category=category)

#     tasks = PostTasks.objects.filter(category__slug=category_slug)

#     if all_posts:
#         context = {
#             'posts': all_posts,
#             'pinned_posts': pinned_posts,  
#             'category': category,
#             'categories': categories,
#         }
#         return render(request, 'main/subcategories.html', context)
#     elif tasks:
#         context = {
#             'tasks': tasks,
#         }
#         return render(request, 'main/all_tasks.html', context)
#     else:
#         context = {
#             'category': category,
#             'categories': categories,
#         }
#         return render(request, 'main/subcategories.html', context)
        

def show_all_tasks(request):
    tasks = PostTasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'main/all_tasks.html', context)
