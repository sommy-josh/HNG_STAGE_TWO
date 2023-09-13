from django.urls import path
from .views import CreatePersonView, RetrieveUpdatePersonView

urlpatterns = [
    path('api/', CreatePersonView.as_view(), name='create-person'),
    path('api/<str:pk>/', RetrieveUpdatePersonView.as_view(), name='retrieve-update-person'),
]
