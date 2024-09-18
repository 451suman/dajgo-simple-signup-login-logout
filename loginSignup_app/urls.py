
from django.urls import path
from loginSignup_app import views

urlpatterns = [
   path("",views.HomeView.as_view(), name="home"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path("demo/", views.DemoView.as_view(), name="demo"),
]
