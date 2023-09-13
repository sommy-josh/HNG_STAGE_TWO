from django.urls import path
from .views import CreatePersonView,RetrieveUpdatePersonView
from . import views

urlpatterns=[
    path('api/persons/', CreatePersonView.as_view(), name='create-person'),
    path('api/persons/<str:name>/', RetrieveUpdatePersonView.as_view(), name='person-detail'),
    path('api/update-person-by-name/<str:name>/', views.UpdatePersonByName.as_view(), name='update-person-by-name'),
]


 

