from item.models import Item
from django import forms


class CreateItem(forms.ModelForm):
    model = Item
    fields = "__all__"