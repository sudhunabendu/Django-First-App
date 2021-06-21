from django.db import models

# Create your models here.

# In this sqlite3 create a database table , so run this command
# python manage.py makemigration
class Contact(models.Model):
  name = models.CharField(max_length=122)
  phone = models.CharField(max_length=12)
  email = models.CharField(max_length=122)
  qus = models.TextField()
  date = models.DateField()

# admin panel a contact list a name dekhte hole ae function ta ke call korte hoye
  def __str__(self):
    return self.name
