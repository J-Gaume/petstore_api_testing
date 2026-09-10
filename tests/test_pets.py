import unittest
import requests
import os
pet = os.environ["pet"]
class PetTestCase(unittest.TestCase):
    
    def test_add_new_pet(self):
        #given 
        djur1 = {
                "id": 100,
                "name": "tester",
                "category": {"id" :12, "name" : "dogs"},
                "status": "pending"
                }
        # when
        anropish = requests.post(f"{pet}/pet", json=djur1)

        #then
        self.assertEqual(200, anropish.status_code)


    def test_hitta_skapat_djur(self):
        #given vi har ett djur skapat

        #when vi söker upp djuret
        animal = requests.get(f"{pet}/pet/100")

        #then 
        self.assertEqual(200, animal.status_code)



    def test_update_pet(self):
        #given pet ska förändras
        djur1_ny = {
                "id": 100,
                "name": "NYTT_NAMN",
                "category": {"id" : 12, "name" : "dogs"},
                "status": "available"
                }
        #when vi genomför anrop
        djur_uppdateras = requests.put(f"{pet}/pet", json=djur1_ny)
        
        #then statuskod 200 för genomförda förändringar
        self.assertEqual(200, djur_uppdateras.status_code)
