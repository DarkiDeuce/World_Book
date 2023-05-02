from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]
