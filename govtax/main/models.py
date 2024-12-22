from django.db import models


class Taxpayer(models.Model):
   GENDER_CHOICES = [
       ('Female', 'Female'),
       ('Male', 'Male'),
   ]
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   date_of_birth = models.DateField()
   gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
   phone = models.CharField(max_length=30)
   home_address = models.CharField(max_length=100)
   total_tax_contribution = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self):
       return f"{self.first_name} {self.last_name}"