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
        
class TestCredentials(unittest.TestCase):
    '''
    it will create the TestCredentials subclass.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials(
            "twitter", "104788W@ve", "DenisLeparteleg")
   
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account, "twitter")
        self.assertEqual(self.new_credentials.password, "104788W@ve")
        self.assertEqual(self.new_credentials.user_name, "DenisLeparteleg") 
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the object is saved in the credentials_list
        '''
        self.new_credentials.save_credentials()
       
        self.assertEqual(len(Credentials.credentials_list), 1)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
    def test_delete_credentials(self):
        '''
        test_delete_credentials test case to test if the credentials details are deleted in the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "104788W@ve", "DenisLeparteleg")  
        test_credentials.save_credentials()
        
    def test_find_credentials_by_password(self):
        '''
        test_find_credentials test case to test if we can find credentials details by password in the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "104788W@ve", "DenisLeparteleg")  
        test_credentials.save_credentials()
        
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "104788W@ve", "DenisLeparteleg") 
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("104788W@ve")

        self.assertTrue(credentials_exists)
        
    def test_display_all_credentials(self):
        '''
        test to display all credentials.
        '''
        self.assertEqual(Credentials.display_all_credentials(),Credentials.credentials_list)
    
    