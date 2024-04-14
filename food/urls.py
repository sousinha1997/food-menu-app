from food import views
from django.urls import path

app_name = "food"
urlpatterns = [
    #/food/
    path("", views.index, name='index'),
    #/food/1
    path('<int:item_id>/', views.detail, name="detail"),
    path("item/", views.item, name='item'),
    # add items
    path("add/",views.create_item, name='create_item'),
    #edit items
    path("update/<int:item_id>/", views.update_item, name='update_item'),
    #delete items
    path("delete/<int:item_id>/", views.delete_item, name='delete_item'),
]