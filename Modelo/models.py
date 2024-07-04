from django.db import models

# Modelo de la aplicacion_ NetZero Elevate web app 
class Industries(models.Model):
    project_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project_name}"

class Services(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.service_name}"

class Team(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f"{self.full_name}"
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"