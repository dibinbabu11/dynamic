from django.db import models

# Create your models here. 

class Featured(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Dibi(models.Model):
    title=models.CharField(max_length=250)
    small=models.CharField(max_length=250)
    description=models.TextField(max_length=2000)
    comments=models.IntegerField()
    def __str__(self):
        return self.title


class Read(models.Model):
    title=models.CharField(max_length=250)
    small=models.CharField(max_length=250)
    description=models.TextField(max_length=2000)
    comments=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.title


class Instagram(models.Model):
    title=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.title