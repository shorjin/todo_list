from django.db import models

# Create your models here.
class Todolist(models.Model):
    text=models.CharField(max_length=45)
    completed=models.BooleanField(default=False)

# return a text representation of the content of the database
    def __str__(self):
        return self.text