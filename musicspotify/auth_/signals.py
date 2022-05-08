from django.db.models import signals
from django.dispatch import receiver
from auth_.models import AuthUser, Profile

@receiver(signal=signals.post_save,
            sender = AuthUser)
def after_create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)