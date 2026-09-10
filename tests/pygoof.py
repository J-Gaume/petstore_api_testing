import requests
import unittest
import os
import time

pet = os.environ["pet"]

class jallan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.KONST = 100


def hello_placeholder():
    goofy = requests.get(f"{pet}/pet/1")
    goofy_data = goofy.json()
    print(goofy_data)

hello_placeholder()
