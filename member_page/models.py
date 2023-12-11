from django.db import models

class TeamMember(models.Model):

    class Role(models.TextChoices):
        REGULAR = "Regular"
        ADMIN = "Admin"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100, 
                            choices=Role.choices,
                            default=Role.REGULAR)
    phone_number = models.CharField(max_length=12)


    def __str__(self):
        return self.first_name+" "+self.last_name