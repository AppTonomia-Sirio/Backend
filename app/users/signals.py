from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import CustomUser, Role


# Signals

# Token creating for NNA and Therapist type users when they are registered

# Create token when user is created
@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)


# Creates 3 roles when the app is started
@receiver(post_migrate)
def create_initial_roles(sender, **kwargs):
    if Role.objects.count() == 0:
        Role.objects.get_or_create(name='NNA')
        Role.objects.get_or_create(name='Therapist')
        Role.objects.get_or_create(name='Admin')
