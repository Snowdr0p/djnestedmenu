from django.urls import path
from . import views
from nested_menu.models import MenuItemContainer

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.index, name='index_1'),
]

# just for testing purposes
for menu_item in MenuItemContainer.objects.all():
    if menu_item.url:
        urlpatterns.append(path(menu_item.url, views.index))
