from django.urls import path


from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<slug:category_slug>/', views.subcategories, name='subcategories'),
    path('all_tasks/', views.show_all_tasks, name='all_tasks'),
]