import unittest 
from credentials import User, Credentials  # Importing the User and Credentials classes
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
                             "denislepartelegke@gmail.com") # create User object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Denis")
        self.assertEqual(self.new_user.last_name, "Leparteleg")
        self.assertEqual(self.new_user.phone_number, "0728982213")
        self.assertEqual(self.new_user.email, "denislepartelegke@gmail.com")
        
    def test_save_user(self):
        '''
        save_user test case to test if the object is saved in the user_list
        '''
        self.new_user.save_user()
    
        self.assertEqual(len(User.user_list), 1)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.user_list = []

    def test_delete_user(self):
        '''
        delete_user test case to test if the object is deleted in the user_list
        '''