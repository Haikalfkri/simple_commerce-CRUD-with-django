from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from item.models import Item
from django.contrib import messages


# Create your views here.
def dashboard(request):
    data = Item.objects.all()
    return render(request, 'dashboard.html', {"items":data})

class CreateItemView(LoginRequiredMixin, CreateView):
    model = Item
    fields = "__all__"
    template_name = "create_item.html"
    success_url = reverse_lazy("item:dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Add item successfully")
        return super(CreateItemView, self).form_valid(form)


class ItemList(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item_list.html"
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        return context
    
    
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item_detail.html"
    

class UpdateItemView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = "__all__"
    template_name = "update_item.html"
    success_url = reverse_lazy("item:home")
    
    def form_valid(self, form):
        messages.success(self.request, "Item update successfully")
        return super().form_valid(form)
    
class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "item_confirm_delete.html"
    success_url = reverse_lazy("item:home")
    
    def form_valid(self, form):
        messages.success(self.request, "Item delete successfully")
        return super().form_valid(form)