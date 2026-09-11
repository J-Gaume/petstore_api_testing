import unittest
import requests
import os
import time
pet = os.environ["pet"]
class PetTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.djur_id = int(time.time())
    
    def test_CREATE_PET(self): 
        djur_id = self.djur_id
        djur1 = {
                "id": djur_id,
                "name": "tester",
                "category": {"id" :12, "name" : "dogs"},
                "status": "pending"
                }
        # when
        anropish = requests.post(f"{pet}/pet", json=djur1)

        #then
        self.assertEqual(200, anropish.status_code)


    def test_FIND_PET(self):
        #given vi har ett djur skapat
        djur_id = self.djur_id

        #when vi söker upp djuret
        animal = requests.get(f"{pet}/pet/{djur_id}")

        #then 
        self.assertEqual(200, animal.status_code)



    def test_UPDATE_PET(self):
        #given pet ska förändras
        djur_id = self.djur_id
        djur1_ny = {
                "id": djur_id,
                "name": "NYTT_NAMN",
                "category": {"id" : 12, "name" : "dogs"},
                "status": "available"
                }
        #when vi genomför anrop
        djur_uppdateras = requests.put(f"{pet}/pet", json=djur1_ny)
        
        #then statuskod 200 för genomförda förändringar
        self.assertEqual(200, djur_uppdateras.status_code)

   # def test_
