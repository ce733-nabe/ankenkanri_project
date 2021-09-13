from django.urls import path
from . import views

app_name = 'akapp'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('anken/create/', views.AnkenCreateView.as_view(), name='anken_create'),
    path('anken/create/complete/', views.AnkenCreateCompleteView.as_view(), name='anken_create_complete'),
    path('anken/list/', views.AnkenListView.as_view(), name='anken_list'),
    path('anken/detail/<int:pk>/', views.AnkenDetailView.as_view(), name='anken_detail'),
    path('anken/update/<int:pk>/', views.AnkenUpdateView.as_view(), name='anken_update'),
    path('anken/delete/<int:pk>/', views.AnkenDeleteView.as_view(), name='anken_delete'),
]