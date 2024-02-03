from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('contact/', views.contact_page, name="contactPage"),
    path('services/', views.services_page, name="servicesPage"),
    path('login/', views.login_page, name="loginPage"),
    path('register/', views.register_page, name="registerPage"),
    path('create/', views.create_garment_schedule_payment, name='create_garment_schedule_payment'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('update/<int:garment_id>/', views.update_garment_schedule_payment, name='update_garment_schedule_payment'),
    path('delete/<int:garment_id>/', views.delete_garment, name='delete_garment'),
    path('display/<int:garment_id>/', views.display_garment, name='display_garment'),

]
