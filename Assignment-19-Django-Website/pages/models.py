from django.db import models


class Registration(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    department = models.CharField(max_length=150)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
