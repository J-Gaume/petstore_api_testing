import unittest
import requests
import os
pet = os.environ["pet"]

class InventoryTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        alla_djur = requests.get(f"{pet}/store/inventory")
        cls.baseline_approved = alla_djur.json()["approved"]
        cls.pet_id = 1000 
    def test_hitta_djur_med_status(self):

        #given det finns flera djur
        alla_djur = requests.get(f"{pet}/store/inventory")
        
        #when vi jämför 
        alla_djur_data = alla_djur.json()

        #then
        self.assertEqual(alla_djur_data["approved"], self.baseline_approved)

    def test_uppdatera_antal_status(self):
        #given vi vet att det finns 50st
        InventoryTestCase.pet_id += 1
        body = {
                "id": InventoryTestCase.pet_id,
                "petId": 100,
                "quantity": 1,
                "status": "approved",
                "complete": True
                }
        # when vi skickar in beställningen
        order = requests.post(f"{pet}/store/order", json=body)

        #anrop ska ge STATUS200
        self.assertEqual(200, order.status_code)
        #and vi kontrollerar att antal uppdaterats
        alla_djur = requests.get(f"{pet}/store/inventory")
        datar = alla_djur.json()
        self.assertEqual(datar["approved"], self.baseline_approved +1)
