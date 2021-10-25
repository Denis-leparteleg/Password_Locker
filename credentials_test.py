import unittest 
from credentials import User, Credentials  
import pyperclip

class TestUser(unittest.TestCase):
    '''
    it will create the Testuser subclass.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Denis", "Leparteleg", "0728982213",
                             "denislepartelegke@gmail.com")