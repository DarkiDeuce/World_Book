from django.contrib import admin
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^books$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),
]
