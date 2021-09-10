from django.urls import path
from . import views

app_name = 'akapp'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('anken/create/', views.AnkenCreateView.as_view(), name='anken_create'),
    path('anken/create/complete/', views.AnkenCreateCompleteView.as_view(), name='anken_create_complete'),
]