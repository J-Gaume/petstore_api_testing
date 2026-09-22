import unittest
import requests
import os
pet = os.environ["pet"]

class UserTestCase(unittest.TestCase):
    
    # klassvariabel ifall test 1 failar ska inte test 2 starta
    post_succeeded = False

    def test_08_CREATE_USER(self):
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
        self.assertEqual(200, register.status_code, f"FAIL!!! STATUS {register.status_code}")
        UserTestCase.post_succeeded = True

    def test_09_USER_FOUND(self):

        if not UserTestCase.post_succeeded:
            self.skipTest(f"TC_08 FAIL")
        #given user has been registered in test 1

        #when anv√ndare kollas upp:
        search = requests.get(f"{pet}/user/bug")

        #then lyckas anropet
        self.assertEqual(200, search.status_code)
        # and namnet i JSON svar i databas = det vi skickade
        self.assertEqual(search.json()["username"], "bug")

    def test_10_USER_LOG_IN(self):
        
        if not UserTestCase.post_succeeded:
            self.skipTest(f"TC_08 FAIL")
        # given anv√ndare har skapats
        params = "?username=bug&password=dev" # <-- GET = ingen body. info i parameters
        # TEST 1 OCH 2 == OK
        
        #when vi ska logga in:
        log_in = requests.get(f"{pet}/user/login{params}")
   
        #then returneras status 200
        self.assertEqual(log_in.status_code, 200)
        #print(log_in.text) <-- sessionsID


    def test_11_USER_UPDATE_OK(self):
        
        #given vi har skapat en user
        if not UserTestCase.post_succeeded:
            self.skipTest(f"TC_08 FAIL!")
        
        #when vi uppdaterar allt except ID:
        updated_user = {
                  "id": 404,
                  "username": "bug_1",
                  "firstName": "internal_1",
                  "lastName": "server_1",
                  "email": "error@gmail.com_1",
                  "password": "dev_1",
                 "phone": "500_1",
                  "userStatus": 2
                  }

        #and genomf√r PUT-anrop med gammal username
        update = requests.put(f"{pet}/user/bug", json = updated_user)
        
        #then mottar vi status 200
        self.assertEqual(200, update.status_code)

    def test_12_OLD_USER_NOT_FOUND(self):
        #given vi har skapat och uppdaterat en user
        if not UserTestCase.post_succeeded:
            self.skipTest(f"TC_08 FAIL!")
        
        #when vi har uppdaterat den (TC-11 OK)

        #then gamla username ej hittas, ger 404
        expected_error = requests.get(f"{pet}/user/bug")
        self.assertEqual(404, expected_error.status_code)


