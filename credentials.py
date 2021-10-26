

class User:
    '''
    It will create User class
    '''
    user_list = []
    def __init__(self, first_name, last_name, phone_number, email):
    
        '''
        It will initialize new instances of the object class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
    def save_user(self):
        User.user_list.append(self)

        '''
        save_user method saves user objects into user_list
        '''
        
    def delete_user(self):
        '''
        delete_user method deletes a saved credentials from the credentials_list
        '''

        User.user_list.remove(self)
        
class Credentials:
    '''
    It will create Credentials class
    '''
    credentials_list = []
    
    def __init__(self, account, password, user_name):
        '''
        __init__ method to initialize the attributes of the class.
        '''
        self.account = account
        self.password = password
        self.user_name = user_name
        
    def save_credentials(self):
        '''
        save_credentials method  that saves a credentials into the credentials_list
        '''
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        '''
        delete_credentials method  that deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a credential that matches that password.
        Args:
            password: password to search for
        Returns :
            Credentials of person that matches the password.
        '''
        
    @classmethod
    def credentials_exist(cls, password):
        '''
        Method that checks if a credentials exists from the contact list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return True

        return False
    
    @classmethod
    def display_all_credentials(cls,credentials):
        '''
        method that returns the credentials list
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.credentials == credentials:
                user_credentials_list.append(credential)
        return user_credentials_list