from django.db import models
import uuid
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length = 25)
    STATUS = (
        ('during','during'),
        ('finished','finished')
    )
    value = models.CharField(max_length=10,choices = STATUS, default='during')
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)


    def __str__(self):
        return self.name 
