from django.urls import path

from .views import *


app_name = "api"

urlpatterns = [
    
    path("qr_code/create/", QrCodeGeneratorJourView.as_view(), name="qr-code-create"),
    path("qr_code/list/", QrCodeGeneratorView.as_view(), name="qr-code-list"),
    path("qr_code/detail/<int:pk>/", DetailQrCodeGeneratorView.as_view(), name="qr-code-detail"),


]