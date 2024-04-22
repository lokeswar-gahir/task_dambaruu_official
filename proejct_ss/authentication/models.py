from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager as AbstractUserManager
# Create your models here.

class UserManager(AbstractUserManager):
  pass

class AdminManager(BaseUserManager):
    def get_queryset(self) -> models.QuerySet:
        query_set = super().get_queryset()
        return query_set.filter(type='ADMIN')

class DefaultUserManager(BaseUserManager):
    def get_queryset(self) -> models.QuerySet:
        query_set = super().get_queryset()
        return query_set.filter(type='USER')


class SuperAdminManager(BaseUserManager):
    def get_queryset(self) -> models.QuerySet:
        query_set = super().get_queryset()
        return query_set.filter(type='SUPER_ADMIN')


class User(AbstractUser):
    class Type(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHER = 'OTHER', 'Other'
    
    default_type = Type.SUPER_ADMIN
    objects = UserManager()
    admin = AdminManager()
    default_user = DefaultUserManager()
    super_admin = SuperAdminManager()

    email = models.EmailField(unique=True)
    type = models.CharField("User Type", max_length=11, choices=Type.choices)
    gender = models.CharField("Gender", max_length=6, choices=Gender.choices)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.default_type
            return super().save(*args, **kwargs)


class Admin(User):
    default_type = User.Type.ADMIN
    # admin = AdminManager()
    
    class Meta:
        proxy=True


class DefaultUser(User):
    default_type = User.Type.USER
    # default_user = DefaultUserManager()

    class Meta:
        proxy=True