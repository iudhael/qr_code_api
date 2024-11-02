from django.urls import path

from .views import *


app_name = "api"

urlpatterns = [
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom-register'),
    path('dj-rest-auth/user/', CustomUserDetailsView.as_view(), name='custom-user-details'),

    path("registre/create/", RegistreView.as_view(), name="registre-create"),
    path("registre/update/<int:pk>/", RegistreUpdateView.as_view(), name="registre-update"),

    path("userinfo/list/", UserInfoView.as_view(), name="userinfo-list"),



    path("qr_code/create/", QrCodeGeneratorJourView.as_view(), name="qr-code-create"),
    path("qr_code/list/", QrCodeGeneratorView.as_view(), name="qr-code-list"),
    path("qr_code/detail/<int:pk>/", DetailQrCodeGeneratorView.as_view(), name="qr-code-detail"),


]