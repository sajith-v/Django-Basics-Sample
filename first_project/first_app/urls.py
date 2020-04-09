from django.urls import path
from first_app import views

app_name = "first_app"
urlpatterns = [
    path('',views.index,name="index"),
    path('form-name',views.form_name,name="form_name"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('register',views.register,name="register")
]
