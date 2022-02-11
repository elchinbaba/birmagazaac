from django.urls import path
from magaza import views

app_name = 'post'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='detail'),
]