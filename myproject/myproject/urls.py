from django.contrib import admin
from django.urls import path
from myapp.views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
]
