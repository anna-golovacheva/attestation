from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(UserManager):
    def _create_user(self, email, password, date_of_birth, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, date_of_birth=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, date_of_birth, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='логин')
    password = models.CharField(max_length=100, verbose_name='пароль')
    email = models.EmailField(unique=True, verbose_name='почта')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateField(auto_now=True, verbose_name='дата редактирования')

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['date_of_birth', 'email']

