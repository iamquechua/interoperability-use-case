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
  
   def save(self, *args, **kwargs):
       if not self.citizen_number:
           count = Citizen.objects.count()
           if count == 0:
                   self.citizen_number = 'C1000'
           else:
               last_citizen = Citizen.objects.last()
               last_citizen_number = int(last_citizen.citizen_number[1:])
               self.citizen_number = f"C{last_citizen_number + 1}"
       super().save(*args, **kwargs)