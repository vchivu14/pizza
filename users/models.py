from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'  
    
def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        
post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)