from rest_framework import authentication, permissions, generics, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import *
from .serializers import *

import qrcode

from django.http import HttpResponse

import uuid

from datetime import datetime

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

class QrCodeGeneratorJourView(generics.ListCreateAPIView):
    serializer_class = QrCodeGeneratorJourSerializer
    queryset = QrCodeJour.objects.all()
    filterset_fields = ["created_at", "nbre_qr"]



    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        #print(data)

        
        qr_code_jour = QrCodeJour.objects.last()
        #print(f"qr jour {qr_code_jour}")
        def crypter_message(message, key):
            cipher = AES.new(key, AES.MODE_ECB)
            encrypted_message = cipher.encrypt(pad(message.encode(), AES.block_size))
            return base64.b64encode(encrypted_message).decode('utf-8')
        
        # Clé secrète pour le chiffrement (doit être de 16, 24 ou 32 octets)
        secret_key = b'macleinsecreten32octets.'  # Exemple de clé en bytes

        
        #print(code_uuid)
        #print(qr_code_jour)
        nbre_qr_code=data['nbre_qr']
        while nbre_qr_code > 0:
            date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            code_uuid = uuid.uuid4()
            #print(code_uuid)
            qr_data = f"scop_{date_heure}_{code_uuid}"
            qr_data_chiffre = crypter_message(qr_data, secret_key)
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=4,
                border=4,
            )
            qr.add_data(qr_data_chiffre)
            qr.make(fit=True)
            qr = qr.make_image(fill_color="#000000", back_color="white").convert('RGB')
            
            # Créez une instance du qr_code et enregistrez-la dans la base de données
            qr_generer = QrCodeGenerator(
                code = qr_data,
                code_chiffre = qr_data_chiffre,
                qr_code_jour = qr_code_jour
            )

            # Enregistrez le qr généré dans qrcodegenerator
            chemin = f"qr_{nbre_qr_code}_{date_heure}.png"
            qr.save(chemin)
            qr_generer.qr_code = chemin

            qr_generer.save()
            nbre_qr_code -= 1

        return response



class QrCodeGeneratorView(generics.ListAPIView):
    serializer_class = QrCodeGeneratorSerializer
    queryset = QrCodeGenerator.objects.all()
    filterset_fields = ["code_chiffre", "code", "qr_code_jour"]


class DetailQrCodeGeneratorView(generics.RetrieveUpdateAPIView):
    serializer_class = QrCodeGeneratorSerializer
    queryset = QrCodeGenerator.objects.all()
