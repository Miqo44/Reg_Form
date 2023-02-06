from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('cars/<str:id>', views.CarListView.as_view(), name='home_detail'),
    path('cars/car/<int:id>', views.CarDetailView.as_view(), name='home_detail_detail'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),



]