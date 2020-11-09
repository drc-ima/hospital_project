from django.urls import *
from .views import *


app_name = 'staff'


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('complaints/', complaints, name='complaints'),
    path('complaint/cancel/<id>/', cancel_complaint, name='complaint-cancel'),
]
