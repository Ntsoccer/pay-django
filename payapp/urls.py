from django.urls import path, include
from . import views

app_name = 'payapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>', views.DetailView.as_view(), name='detail'),
]
