from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', height_field=None, width_field=None, max_length=None)
    

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural =("Profiles")

    def __str__(self):
        return str(self.user)

