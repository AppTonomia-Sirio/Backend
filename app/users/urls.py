from django.urls import path
from .views import (
    LoginView,
    UserCreate,
    HomeListView,
    RoleListView,
    CurrentUserView,
    UserListView,
    UserDetailView,
    HomeView,
    RoleView,
    UserChangeStatusView

)

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:id>/', UserDetailView.as_view()),
    path('<int:id>/status', UserChangeStatusView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', UserCreate.as_view()),
    path('home/<int:id>', HomeView.as_view()),
    path('homes/', HomeListView.as_view()),
    path('roles/<int:id>', RoleView.as_view()),
    path('roles/', RoleListView.as_view()),
    path('current/', CurrentUserView.as_view()),
]
