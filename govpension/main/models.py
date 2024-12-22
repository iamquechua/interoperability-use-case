from django.db import models


class Retiree(models.Model):
   SEX_CHOICES = [
       ('Female', 'Female'),
       ('Male', 'Male'),
   ]
   first_name = models.CharField(max_length=100)
   middle_name = models.CharField(max_length=100)
   family_name = models.CharField(max_length=100)
   birth_date = models.DateField()
   sex = models.CharField(max_length=10, choices=SEX_CHOICES)
   mobile_number = models.CharField(max_length=30)
   physical_address = models.CharField(max_length=100)
   total_tax_contribution = models.DecimalField(max_digits=10, decimal_places=2)
   yearly_pension_allowance = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self):
       return f"{self.first_name} {self.family_name}"