from django.db import models

# Create your models here.

class OfficialName(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length = 15, null=False)
    position = models.CharField(null=False)
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    