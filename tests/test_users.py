import unittest
import requests
import os
pet = os.environ["pet"]

class UserTestCase(unittest.TestCase):
    
    # klassvariabel ifall test 1 failar ska inte test 2 starta
    post_succeeded = False

    def test_1_add_new_user(self):
        #given vi har giltiga uppgifter
        new_user = {
                "id": 404,
                "username": "bug",
                "firstName": "internal",
                "lastName": "server",
                "email": "error@gmail.com",
                "password": "dev",
                "phone": "500",
                "userStatus": 1
                }

        #when vi registrerar ny user
        register = requests.post(f"{pet}/user", json=new_user)

        #then ser vi status 200 OK
        self.assertEqual(200, register.status_code, f"TEST FAILED, STATUS {response.status_code}")
        UserTestCase.post_succeeded = True

    def test_2_new_user_registered(self):
        
        if not UserTestCase.post_succeeded == True:
            self.skipTest(f"SKIPPAR TEST PGA TEST 1 FAIL.")
        #given user has been registered in test 1

        #when anv√ndare kollas upp:
        search = requests.get(f"{pet}/user/bug")

        #then lyckas anropet
        self.assertEqual(200, search.status_code)
        # and namnet i JSON svar i databas = det vi skickade
        self.assertEqual(search.json()["username"], "bug")
