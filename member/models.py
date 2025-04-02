from django.db import models

# Create your models here.
class Member(models.Model):
    memberName=models.CharField(max_length=255)
    memberPhone = models.IntegerField(null=True)
    memberJoinDate = models.DateField(null=True)


    def __str__(self):
        return f"{self.memberName}"