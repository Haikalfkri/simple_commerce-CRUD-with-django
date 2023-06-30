from django.contrib import admin
from item.models import Category, Item
from django.utils.html import format_html


class ImageItem(admin.ModelAdmin):
    
    def img(self, obj):
        return format_html("<img src='{}' style='height: 200px; width: 200px;'>".format(obj.image.url))

    
    list_display = ['title', 'img']

# Register your models here.
admin.site.register(Category)
admin.site.register(Item, ImageItem)