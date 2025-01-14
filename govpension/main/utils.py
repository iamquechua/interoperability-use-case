import requests
from main.models import Citizen, RetireeProfile, TaxpayerProfile # updated



def load_data_from_api(endpoint):
   response = requests.get(endpoint)
   return response.json()
 

def load_citizens_from_api():
   data = load_data_from_api('http://127.0.0.1:8030/api/citizens/')
   for citizen in data:
       Citizen.objects.create(
           first_name=citizen['first_name'],
           middle_name=citizen['middle_name'],
           last_name=citizen['last_name'],
           citizen_number=citizen['citizen_number'],
           date_of_birth=citizen['date_of_birth'],
           gender=citizen['gender'],
           phone_number=citizen['phone_number'],
           address=citizen['address'],
       )


def load_taxpayers_from_api():
   data = load_data_from_api('http://127.0.0.1:8010/api/taxpayers/')
   for taxpayer in data:
       TaxpayerProfile.objects.create(
           citizen=Citizen.objects.get(citizen_number=taxpayer['citizen_number']),
           total_tax_contribution=taxpayer['total_tax_contribution'],
       )

# new
def create_retiree_profiles(taxpayers):
   for taxpayer in taxpayers:
       RetireeProfile.objects.create(
           citizen=Citizen.objects.get(citizen_number=taxpayer.citizen.citizen_number),
           yearly_pension_allowance=taxpayer.total_tax_contribution / 10,
       )

