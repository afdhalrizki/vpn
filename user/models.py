from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.abstract_models import TimestampedAbstract
from company.models import IndustryChoices

class UserTypeChoices(models.TextChoices):
    OWNER = ('OWNER', 'OWNER')
    EMPLOYEE = ('EMPLOYEE', 'EMPLOYEE')

class UserTimestampedAbstract(TimestampedAbstract):
    updated_by = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='%(class)s_updated_by', null=True, blank=True)
    created_by = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='%(class)s_created_by')
    
    class Meta:
        abstract=True

class CompanyOwnershipAbstract(UserTimestampedAbstract):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='%(class)s_entities')
    
    class Meta:
        abstract=True

class Company(UserTimestampedAbstract):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200, choices=IndustryChoices.choices)

    def __str__(self):
        return self.name

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee', null=True, blank=True)
    user_type = models.CharField(max_length=10, null=False, blank=False, choices=UserTypeChoices.choices)