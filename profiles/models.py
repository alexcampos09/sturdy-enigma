# Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# def upload_location(instance, filename):
#     return "%s/Profile/%s" %(instance.user, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # image = models.ImageField(
    #     upload_to = upload_location,
    #     blank=True,
    #     null=True,
    #     verbose_name = 'Foto de Perfil',
    #     width_field="width",
    #     height_field="height",
    # )

    def get_absolute_url(self):
        return f"/profiles/{self.pk}"

    def __str__(self):
    	return self.user.email

    class Meta:
    	db_table = 'profiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()
