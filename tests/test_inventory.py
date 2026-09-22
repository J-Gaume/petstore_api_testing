import unittest
import requests
import os
pet = os.environ["pet"]
import time

class InventoryTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        alla_djur = requests.get(f"{pet}/store/inventory")
        cls.baseline_approved = alla_djur.json()["approved"]
        cls.pet_id = int(time.time())

    def test_04_FIND_PETS_BY_STATUS(self):

        #given det finns flera djur
        alla_djur = requests.get(f"{pet}/store/inventory")
        
        #when vi j√§mf√∂r 
        alla_djur_data = alla_djur.json()

        #then
        self.assertEqual(alla_djur_data["approved"], self.baseline_approved)

    def test_05_CREATE_ORDER(self):
        #given vi vet att det finns 50st
        #InventoryTestCase.pet_id += 1
        body = {
                "id": InventoryTestCase.pet_id,
                "petId": 100,
                "quantity": 1,
                "status": "approved",
                "complete": True
                }
        # when vi skickar in best√§llningen
        order = requests.post(f"{pet}/store/order", json=body)

        #anrop ska ge STATUS200
        self.assertEqual(200, order.status_code)
        
    def test_06_PLACED_ORDER_FOUND(self):  # kontrollerar f√reg√ende test
        #given vi har skapat ett djur

        #when vi s√∂ker upp antalet
        alla_djur = requests.get(f"{pet}/store/inventory")
        datar = alla_djur.json()

        #then s√ kommer antalet ha uppdaterats korrekt
        self.assertEqual(datar["approved"], self.baseline_approved +1)

    def test_07_ORDER_FOUND_BY_ID(self):
        pet_id = self.pet_id

        #given vi har ett djur skapat
        
        #when vi s√ker p√•ett djur:
        search = requests.get(f"{pet}/store/order/{pet_id}")

        #then hittar vi djuret och tar emot status 200
        self.assertEqual(200, search.status_code)
