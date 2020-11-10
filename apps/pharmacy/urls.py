from django.urls import path
from .views import *

app_name = 'pharmacy'


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('medicines/', Medicines.as_view(), name='medicines'),
    path('treatments/', Treatments.as_view(), name='treatments'),
    path('treatment/<id>/', TreatmentDetails.as_view(), name='treatment-details'),
    path('medicine/<id>/', MedicineDetails.as_view(), name='medicine-details'),
]
