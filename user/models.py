from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.functional import cached_property


class CustomAccountManager(BaseUserManager):

    def _create_user(self, email, password, **other_fields):
        """create and saves the user with the given info"""

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_active', True)

        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self._create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    discount = models.IntegerField(default=0)
    
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(
        max_length=50, default='', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, default='', null=True, blank=True)
    state = models.CharField(max_length=30, default='', null=True, blank=True)
    phone = models.CharField(max_length=15, default='', null=True, blank=True)
    zip_code = models.CharField(max_length=15, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
