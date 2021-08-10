from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),


    path('region/<str:pk>/', BlogRegionListView, name='region'),
    path('category/<str:pk>/', BlogCategoryListView, name='category'),


    path('profile/', profile, name='profile'),
    path('edit_profile/', BlogEditUserView, name='edit_profile'),


    path('create/', BlogCreateView, name='create'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', BlogEditView.as_view(), name='edit'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]
