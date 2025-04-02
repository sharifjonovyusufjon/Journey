from django.db import models

# Create your models here.
class Travel(models.Model):
    travelTitle=models.CharField(max_length=400)
    travelDesc=models.CharField(max_length=1000)
    travelAddress=models.CharField(max_length=300)
    travelImg=models.CharField(max_length=500)

    def __str__(self):
        return f"{self.travelTitle}"