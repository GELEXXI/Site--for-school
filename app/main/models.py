from django.db import models

# Create your models here.
class Categories(models.Model):
    img = models.ImageField(upload_to='cat',verbose_name='Фото категории', blank=True,)
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def get_subcategories(self):
        return Categories.objects.filter(parent_category=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

class PostTasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    answer =models.TextField(blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Задачі'
        verbose_name = 'Задача'
        ordering = ['title']
# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
#     name = models.CharField(max_length=25, unique=True, verbose_name='Название')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'ПодКатегории'
#         verbose_name = 'ПодКатегория'
#         ordering = ['name']