from django.db import models

# Create your models here.
class email(models.Model):
    mail = models.EmailField()
    
    def __str__(self):
        return self.mail
    