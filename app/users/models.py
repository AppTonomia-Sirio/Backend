from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .validators import DocumentValidator, PasswordValidator
from django.db import models


# Create your models here
class CustomUserManager(BaseUserManager):
    # Custom user manager for CustomUser model

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Custom user model
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=True, null=True, validators=[PasswordValidator()])
    document = models.CharField(max_length=255, blank=True, null=True, validators=[DocumentValidator()])
    date_of_birth = models.DateField(blank=True, null=True)
    home = models.ForeignKey('Home', on_delete=models.CASCADE, blank=True, null=True)
    roles = models.ManyToManyField('Role', blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Frozen', 'Frozen'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email


class Home(models.Model):
    # Location model

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    # Role model

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
