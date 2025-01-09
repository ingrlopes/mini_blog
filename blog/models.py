from django.db import models
from django.contrib.auth.models import User  # Adicione esta linha

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # Permite valores nulos e em branco

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Use a classe User importada
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Remove a permissão para valores nulos

    def __str__(self):
        return self.title
