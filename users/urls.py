from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers, name="get_users"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='get_profile'),
    path('register/', views.registerUser, name='register'),
    path('<str:pk>/', views.getUserById, name='get_user'),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
]
