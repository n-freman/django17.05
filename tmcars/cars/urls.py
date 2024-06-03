from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='cars'),
    path("<int:pk>", views.car, name='car-object'),
    path("my-cars", views.my_cars, name='my-cars'),
    path("add", views.add_car, name='add-car'),
    path("edit/<int:pk>", views.edit_car, name='edit-car'),
    path("delete/<int:pk>", views.delete_car, name='delete-car'),
    path("search", views.search, name='search-car'),
    path("search-results", views.search_results, name='car-search-results'),
]
