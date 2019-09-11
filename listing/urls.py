from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="listing_index"),
    path('<int:listing_id>', views.show, name="listing_show"),
    path('search', views.search, name="listing_search"),
]
