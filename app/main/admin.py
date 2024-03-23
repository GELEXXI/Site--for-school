from django.contrib import admin

from main.models import Categories,PostTasks

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