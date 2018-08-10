from django.urls import path
from .views import post_model_list_view, post_model_detail_view

urlpatterns = [
    path('', post_model_list_view, name="list"),
    path('<int:id>/', post_model_detail_view, name="detail"),
]
