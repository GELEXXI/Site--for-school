from django.contrib import admin

from main.models import Categories,PostTasks,Post

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(PostTasks)
class PostTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed','answer','category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Post)
class PostTaskAdmin(admin.ModelAdmin):
    list_display = ('title',  'content','category','is_visible','created_at',)
    list_filter = ('category','id')
    search_fields = ('title', 'content')