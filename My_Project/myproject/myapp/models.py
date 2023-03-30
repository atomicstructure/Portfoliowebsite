from django.db import models



# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    
