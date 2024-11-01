# Generated by Django 4.2.16 on 2024-11-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QrCodeJour",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="date et heure de generation du qr code",
                    ),
                ),
                (
                    "nbre_qr",
                    models.IntegerField(
                        verbose_name="nombre de qr code par generation"
                    ),
                ),
            ],
            options={"verbose_name": "qr_code jour",},
        ),
        migrations.CreateModel(
            name="QrCodeGenerator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "qr_code",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="QR code"
                    ),
                ),
                (
                    "code",
                    models.UUIDField(
                        unique=True, verbose_name="code de verification du qr code"
                    ),
                ),
                (
                    "code_chiffre",
                    models.TextField(
                        verbose_name="code de verification du qr code chiffrer"
                    ),
                ),
                (
                    "qr_code_jour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.qrcodejour"
                    ),
                ),
            ],
            options={"verbose_name": "qr_code generer",},
        ),
    ]