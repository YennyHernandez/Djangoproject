from django.db import models    

# Create your models here.
class Project(models.Model): #tabla llamada project 
    name = models.CharField(max_length=200 )  #propiedades de la tabla. charfiedl indica que va a ser un texto

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)