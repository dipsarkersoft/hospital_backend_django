from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from patient.models import Patient


class Speacialization(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=60)

    def __str__(self):
        return f"{self.name}"
    

class Desigation(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=60)

    def __str__(self):
        return f"{self.name}"
    



class AvailableTime(models.Model):
    name=models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.name}"



class Doctor(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='doctor/images')
    designation =models.ManyToManyField(Desigation)
    specialization=models.ManyToManyField(Speacialization)
    available_time =models.ManyToManyField(AvailableTime)
    fee =models.IntegerField()
    meet_link =models.CharField(max_length=50)


    def __str__(self):
       return f"{self.user.first_name} {self.user.last_name}"



STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    star=models.CharField(max_length=30,choices=STAR_CHOICES)

    def __str__(self):
       return f"Reviewer {self.reviewer.user.first_name} Doctor {self.doctor.user.first_name}"

