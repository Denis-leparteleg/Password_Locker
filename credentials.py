


class User:
    
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