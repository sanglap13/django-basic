from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class workType(models.Model):
    WORK_TYPE = [
        ('Web', 'Web Development'),
        ('Mob', 'Mobile Development'),
        ('UX', 'UI/UX Design'),
        ('DM', 'Digital Marketing'),
        ('CW', 'Content Writing'),
        ('GD', 'Graphic Design'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="workType/")
    date_added = models.DateTimeField(default=timezone.now)
    work_type = models.CharField(max_length=3, choices=WORK_TYPE)
    description = models.TextField(default="")
    
    def __str__(self):
        return self.name