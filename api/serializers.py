from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import *

class QrCodeGeneratorJourSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QrCodeJour
        fields = "__all__"


class QrCodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCodeGenerator
        fields = "__all__"
        read_only_fields = ['qr_code', 'code', 'code_chiffre', 'qr_code_jour']