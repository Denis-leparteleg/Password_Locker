#!/usr/bin/env python3.9
from credentials import User, Credentials

def create_user(first_name, last_name, phone_number, email):
    '''
    Function to create a new user
    '''
    new_user = user(first_name, last_name, phone_number, email)
    return new_user


def save_user(user_name):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def create_credentials(account, password, user_name):
    '''
    Function to create a new credentials
    '''
    new_credentials = credentials(account, password, user_name)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(credentials):
    '''
    Function that finds a credentials by email and returns the password
    '''
    return credentials.find_by_password(password)


def check_existing_email(password):
    '''
    Function that check if a email exists with that password and return a Boolean
    '''
    return Credentials.credentials_exist(password)