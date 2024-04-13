from django import forms
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from main.models import Categories,PostTasks,Post

# admin.site.register(Categories)
# admin.site.register(Products)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget)
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name","parent_category")

@admin.register(PostTasks)
class PostTaskAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_completed', 'answer', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_visible','is_favorite','is_pinned','content','created_at')
    list_filter = ('category','id')
    search_fields = ('name', 'content')