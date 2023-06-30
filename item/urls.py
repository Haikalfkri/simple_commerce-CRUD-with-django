from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.ItemList.as_view(), name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/", views.CreateItemView.as_view(), name="create_item"),
    path("detail/<int:pk>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("edit/<int:pk>/", views.UpdateItemView.as_view(), name="edit_item"),
    path("delete/<int:pk>", views.ItemDelete.as_view(), name="item_delete"),
]
