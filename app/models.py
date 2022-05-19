from django.db import models
from datetime import datetime

# Create your models here.
class Auth(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=16)
    project_id = models.CharField(max_length=30)
    private_key_id = models.CharField(max_length=50)
    private_key = models.CharField(max_length=1800)
    client_email  = models.CharField(max_length=60)
    client_id = models.CharField(max_length=30)
    auth_uri = models.CharField(max_length=45)
    token_uri = models.CharField(max_length=50)
    auth_provider_x509_cert_url = models.CharField(max_length=50)
    client_x509_cert_url = models.CharField(max_length=250)

    def __str__(self): 
        return self.project_id

class Url(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Status(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    status= models.IntegerField(default=-1)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.url.url}:{self.status}"
