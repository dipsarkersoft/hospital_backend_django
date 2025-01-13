from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_num=models.CharField(max_length=12)
    image=models.ImageField(upload_to='patient/uploads')


    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"
    