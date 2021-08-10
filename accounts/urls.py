from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView, name='signup')
]
