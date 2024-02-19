from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers, name="get_users"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='get_profile'),
    path('<str:pk>/', views.getUserById, name='get_user'),

]
