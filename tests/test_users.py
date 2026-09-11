import unittest
import requests
import os
pet = os.environ["pet"]

class UserTestCase(unittest.TestCase):
    
    # klassvariabel ifall test 1 failar ska inte test 2 starta
    post_succeeded = False

    def test_1_create_new_user(self):
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

        #then ser vi status 200 OK                  #tredje argument = felmeddelande
        self.assertEqual(200, register.status_code, f"FAIL!!! STATUS {response.status_code}")
        UserTestCase.post_succeeded = True

    def test_2_registration_OK(self):

        if not UserTestCase.post_succeeded:
            self.skipTest(f"SKIP - TC_01 FAIL")
        #given user has been registered in test 1

        #when anv√ndare kollas upp:
        search = requests.get(f"{pet}/user/bug")

        #then lyckas anropet
        self.assertEqual(200, search.status_code)
        # and namnet i JSON svar i databas = det vi skickade
        self.assertEqual(search.json()["username"], "bug")

    def test_3_user_kan_loggas_in(self):
        
        if not UserTestCase.post_succeeded:
            self.skipTest(f"SKIP - TC_01 FAIL")
        params = "?username=bug&password=dev" # <-- GET = ingen body. info i parameters
        
        #given en user har skapats
        # TEST 1 OCH 2 == OK
        
        #when vi ska logga in:
        log_in = requests.get(f"{pet}/user/login{params}")
   
        #then returneras status 200
        self.assertEqual(log_in.status_code, 200)
        #print(log_in.text) <-- sessionsID

