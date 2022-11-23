from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_outside = models.BooleanField(default=False)
    can_add_user = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Document(models.Model):
    document_name = models.CharField(max_length=50)
    sender = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    recipient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    recipient_name = models.CharField(max_length=50, null=True, blank=True)
    document_description = models.TextField()
    is_sent = models.BooleanField(null=True)
    is_received = models.BooleanField(null=True)
    date_sent = models.DateTimeField(null=True, blank=True)
    document_content = models.FileField(upload_to="./static/files/", null=True)




def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
