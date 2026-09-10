import requests
import unittest
import os
import time

pet = os.environ["pet"]

class jallan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.KONST = 100

    def test_add_user(self):
        #given user has valid data
        konst = self.KONST + 1
        new_user = {
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}

        my_user = {
                "id": 213,
                "username": "dev",
                "firstName": "Johan",
                "lastName": "Giz",
                "email": "yoyoyo@gmail.com",
                "password": "dev",
                "phone": "112",
                "userStatus": 1
                }
        #when data is posted to correct endpoint
        send_post = requests.post(f"{pet}/user", json=new_user)

        #then status 200
        self.assertEqual(200, send_post.status_code)

    def test_user_in_database(self):
        #given user exists

        #when we search user
        search = requests.get(f"{pet}/user/dev")
        
        #then request is successful
        self.assertEqual(200, search.status_code)
        
    def test_cls_funkish(self):
        konst = self.KONST
        print(konst)


    def test_hello_placeholder(self):
        goofy = requests.get(f"{pet}/pet/1")
        goofy_data = goofy.json()
        print(goofy_data)

if __name__ == "__main__":
    unittest.main()
