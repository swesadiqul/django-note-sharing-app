from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=200)


    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-full_name']