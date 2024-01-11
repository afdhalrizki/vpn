from django.db import models

class IndustryChoices(models.TextChoices):
    FINTECH = ('FINTECH', 'FINTECH')
    EDUTECH = ('EDUTECH', 'EDUTECH')
    ECOMMERCE = ('ECOMMERCE', 'ECOMMERCE')