from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import *
from dj_rest_auth.registration.serializers import RegisterSerializer

class QrCodeGeneratorJourSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QrCodeJour
        fields = "__all__"


class QrCodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCodeGenerator
        fields = "__all__"
        read_only_fields = ['qr_code', 'code', 'code_chiffre', 'qr_code_jour']






class CustomRegisterSerializer(RegisterSerializer):
    #first_name = serializers.CharField(min_length=3, max_length=50, required=True)
    #last_name = serializers.CharField(min_length=3, max_length=50, required=True)
    username = serializers.CharField(min_length=4, max_length=50, required=True)
    password1 = serializers.CharField(style={'input_type' : 'password'}, write_only =True)
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only =True)

    user_info_qr_code_genere = serializers.CharField(min_length=3)
    
    class Meta:
        model = User  # Remplacez par le nom de votre modèle utilisateur
        #fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', "user_info_qr_code_genere")
        fields = ('username', 'email', 'password1', 'password2', "user_info_qr_code_genere")


    """
    def validate_password1(self, value):
        regex_pattern = "(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z]).{8,}"
        if not re.match(regex_pattern, value):
            raise serializers.ValidationError("Le mot de passe ne suit pas le format requis : au moins 8 caractères, au moins une majuscule, au moins un chiffre.")
        return value
    """


    def custom_signup(self, request, user):
        #user.first_name = self.validated_data.get('first_name', '')
        #user.last_name = self.validated_data.get('last_name', '')
        qr_code_genere = self.validated_data.get('user_info_qr_code_genere', '')
        
        qr = QrCodeGenerator.objects.get(code_chiffre=qr_code_genere)
        print(qr)

        user.save()
        
        Userinfo.objects.create(user=user, qr_code_genere=qr)

class CustumUserSerializer(serializers.ModelSerializer):

    user_info_id = serializers.CharField(source='userinfo.id', read_only=True)
    user_info_qr_code_genere = serializers.CharField(source='userinfo.qr_code_genere', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_info_id', 'user_info_qr_code_genere')




class RegistreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registre
        fields = "__all__"
        
#afficher les infos 
class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Userinfo
        fields = ("id", "user", "qr_code_genere")
        read_only_fields = ['user']