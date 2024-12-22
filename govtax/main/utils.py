from main.models import Citizen


def load_citizens_from_api():
   import requests
   ENDPOINT = 'http://127.0.0.1:8030/api/citizens/'
   response = requests.get(ENDPOINT)
   data = response.json()
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
