from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class House(models.Model):
    address = models.TextField()
    price = models.TextField()
    room_count = models.IntegerField(default=1)
    contract_end_date = models.DateField()
    property_type = models.TextField()
    parking_space_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.address


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password"""
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.TextField()
    email = models.TextField(unique=True)
    location = models.TextField()
    destination = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
