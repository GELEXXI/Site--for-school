from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Categories(models.Model):
    img = models.ImageField(upload_to='cat',verbose_name='Фото категории', blank=True,)
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    is_favorite = models.BooleanField(default=False)

    def get_subcategories(self):
        return Categories.objects.filter(parent_category=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']
        
class Post(models.Model):
    
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='post',verbose_name='Фото поста', blank=True,)
    # content = models.TextField()
    content=CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='POST_URL')
    is_visible = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пости'
        verbose_name = 'Пост'
        ordering = ['id']

class PostTasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    answer =CKEditor5Field('Text', config_name='extends',blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Задачі'
        verbose_name = 'Задача'
        ordering = ['name']

class PinnedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pinned Post: {self.post.name} ({self.category.name})"
    

@receiver(post_save, sender=Post)
def update_pinned_post(sender, instance, created, **kwargs):
    if created:
        # Якщо створено новий пост, не робимо нічого
        return
    
    # Якщо пост змінено, перевіряємо, чи він є закріпленим
    pinned = PinnedPost.objects.filter(post=instance).exists()
    if not pinned and instance.is_pinned:
        # Якщо пост став закріпленим, створюємо запис в моделі PinnedPost
        PinnedPost.objects.create(post=instance, category=instance.category)
    elif pinned and not instance.is_pinned:
        # Якщо пост був закріплений і став не закріпленим, видаляємо запис з моделі PinnedPost
        PinnedPost.objects.filter(post=instance).delete()

@receiver(post_delete, sender=PinnedPost)
def delete_pinned_post(sender, instance, **kwargs):
    # При видаленні запису з моделі PinnedPost, перевіряємо, чи пост все ще існує
    if instance.post:
        instance.post.is_pinned = False
        instance.post.save()