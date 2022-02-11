from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'magaza'

urlpatterns = [
    path('', magaza, name='magaza'),
    path('create/', create, name='create'),
    path('<slug:slug>/', include('magaza.post.urls')),
]