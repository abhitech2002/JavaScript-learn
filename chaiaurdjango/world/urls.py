from django.urls import path
from . import views

urlpatterns = [
    path('', views.learn, name='learn'),
    path('<int:chai_id>/', views.detail, name='detail'),
]