#! /usr/bin/python
# -*- encoding: utf-8 -*-

from services.token import TokenService

class AuthModel(object):
    
    def __init__(self, username, password):

        self.token = TokenService.get_token(username, password)
    
    def get_headers(self):
        return {'Authorization': f'Bearer {self.token.access_token}'}
        
    def __str__(self):
        return f"{self.token}"
        


