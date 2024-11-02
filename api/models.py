from django.db import models
import os, shutil
from PIL import Image
from django.core.validators import MinValueValidator
from datetime import datetime
from django.contrib.auth.models import User

#information sur le nombre de qr_code generer par jour
class QrCodeJour(models.Model):
    created_at = models.DateTimeField("date et heure de generation du qr code", auto_now_add=True)
    nbre_qr = models.IntegerField("nombre de qr code par generation", validators=[MinValueValidator(1)], )


    class Meta:
        verbose_name = "qr_code jour"

    def __str__(self):
        return str(self.id)
    




class QrCodeGenerator(models.Model):
    qr_code = models.ImageField("QR code", null=True, blank=True)
    code = models.TextField("code de verification du qr code", unique=True)
    code_chiffre = models.TextField("code de verification du qr code chiffrer", unique=True) #le code a ete chiffre avec une cle secrete

    qr_code_jour = models.ForeignKey(QrCodeJour, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = "qr_code generer"

    def __str__(self):
        return str(self.id)


    def save(self, *args, **kwargs): # remplacer la methode de sauvegarde por ajouter des fonctionaliter au save parent
        super(QrCodeGenerator, self).save(*args, **kwargs)
        date_actuelle= datetime.now().strftime("%Y-%m-%d")
        

        #chemin actuel de l'image
        
        chemin_actuel_qr = str(self.qr_code)

        print(chemin_actuel_qr)
        
        
        picture_name_qr=  chemin_actuel_qr.split('/')[-1]
        print(picture_name_qr)
        
        
        new_dossier = f'media/qr_code_{date_actuelle}'
        print(new_dossier)
        
        #chemin par defaut de l'enregistrement de l'image 
        
        default_chemin_qr =f'{picture_name_qr}'
        print(default_chemin_qr)
        
        #nouveau chemin de l'enregistrement de l'Image
        
        new_chemin_qr =f'media/qr_code_{date_actuelle}/{picture_name_qr}'
        
        
        if not os.path.isdir(new_dossier):
            os.makedirs(new_dossier)
            
        if os.path.isfile(default_chemin_qr):
            new_chemin_actuel_qr = f'qr_code_{date_actuelle}/{picture_name_qr}'
            shutil.move(default_chemin_qr, new_chemin_qr)
            self.qr_code = new_chemin_actuel_qr
            self.save()


class Userinfo(models.Model):
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    qr_code_genere = models.OneToOneField(QrCodeGenerator, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "User info"

    def __str__(self):
        return str (self.user.pk) + " " +self.user.username
    
ARRIVE= 'arrive'
SORTIE = 'sortie'


STATUS_CHOICES = [
    (ARRIVE, 'ARRIVE'),
    (SORTIE, 'SORTIE'),

]
class Registre(models.Model):
    created_at = models.DateField("date ", auto_now_add=True)
    heure = models.TimeField("heure d'arrivée ou de depart", auto_now_add=True)
    eta = models.CharField("Arrivé ou sortie", max_length=10, choices=STATUS_CHOICES, null=True, blank=True)
    motif = models.CharField("motif ", max_length=20, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = "Registre"

    def __str__(self):
        return str (self.user.pk) + " " +self.user.username