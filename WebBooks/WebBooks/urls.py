from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from catalog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]
