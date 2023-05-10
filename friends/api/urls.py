from django.urls import path
from . import views

urlpatterns = [
    path('', views.FriendListCreateView.as_view(), name='friend-list-create'),
    path('<int:pk>/', views.FriendRetrieveUpdateDestroyView.as_view(), name='friend-retrieve-update-destroy'),
]
