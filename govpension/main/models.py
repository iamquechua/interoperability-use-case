from django.db import models



class Citizen(models.Model):
   GENDER_CHOICES = [
       ('Female', 'Female'),
       ('Male', 'Male'),
   ]
   citizen_number = models.CharField(max_length=10, unique=True, editable=False)
   first_name = models.CharField(max_length=100)
   middle_name = models.CharField(max_length=100, blank=True)
   last_name = models.CharField(max_length=100)
   date_of_birth = models.DateField()
   gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
   phone_number = models.CharField(max_length=30)
   address = models.CharField(max_length=100)


   def __str__(self):
       full_name = f"{self.first_name} {self.last_name}"
       if self.middle_name:
           full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
       return full_name
  


class TaxpayerProfile(models.Model):
   citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, related_name='taxpayer_profile'
)
   total_tax_contribution = models.DecimalField(max_digits=10, decimal_places=2)


   def __str__(self):
       return f"Taxpayer Profile of {self.citizen}"




class RetireeProfile(models.Model):
   citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, related_name='retiree_profile'
)
   yearly_pension_allowance = models.DecimalField(max_digits=10, decimal_places=2)


   def __str__(self):
       return f"Retiree Profile of {self.citizen}"