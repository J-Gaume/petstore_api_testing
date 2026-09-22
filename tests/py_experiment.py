import requests
import unittest
import os
import time

pet = os.environ["pet"]

#class jallan(unittest.TestCase):

def test_3_user_kan_loggas_in():
    params = "?username=bug&password=dev"    
    #given en user har skapats
    # TEST 1 OCH 2 == OK
    
    #when vi ska logga in:
    log_in = requests.get(f"{pet}/user/login{params}")
        
    #then returneras status 200
    self.assertEqual(log_in.status_code, 200)
        
    #print(log_in.text) <-- sessionsID

if __name__ == "__main__":
    unittest.main()
