from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=256)
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.category


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title