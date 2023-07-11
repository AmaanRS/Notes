from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from ckeditor.fields import RichTextField

# Create your models here.
class User_profile(models.Model):
    # The below commented fields are not necessary as they are already defined in User model
    # id = models.AutoField(primary_key=True)
    # Username = models.CharField(max_length=10,default="")
    # Password = models.CharField(max_length=20,default="")
    # Email = models.CharField(max_length=20,default="")
    Image = models.ImageField(upload_to='Notes/Notes/media/Notepad',default='Notepad/default_user_img.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")

# Using OneToOne relationship of database join User model of django and custom model User_profile
# This function runs afer a user object is saved ie post_save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=130,default='Note')
    Last_edited = models.DateTimeField(auto_now=True)
    Image = models.ImageField(upload_to='Notes/Notes/media/Notepad', default='Notepad/default_notes-img.jpg')
    Text = models.CharField(max_length=1000000,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.Title