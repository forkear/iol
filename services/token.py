#! /usr/bin/python
# -*- encoding: utf-8 -*-

import requests
import pprint
from models import *
import config 
import json

class Token(object):

    def __init__(self, access_token = "", issued = None, expires = None, refreshexpires = None, expires_in = None, refresh_token ="", token_type = 'bearer'):
        self.access_token = access_token
        self.issued = issued
        self.expires =expires
        self.refreshexpires = refreshexpires
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.token_type = token_type

    def __str__(self):
        return f"TOKEN:\n\naccess_token: {self.access_token} \n\nrefresh_token: {self.refresh_token}"



class TokenService(object):

    
    @classmethod
    def get_token(cls, username, password):
        
        headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'}

        url = f"{config.API_URL}/token"

        params = {
            'username':username,
            'password':password,
            'grant_type':'password',
        }

        r = requests.post(url, data=params, headers=headers)

        if r.status_code != 200:
            raise Exception(f'No podemos obtener el token {r.status_code}')

        data = r.json()

        token = Token(access_token=data['access_token'], 
                        issued=data['.issued'], 
                        expires=data['.expires'], 
                        refreshexpires=data['.refreshexpires'],
                        expires_in=data['expires_in'],
                        refresh_token=data['refresh_token'],
                        token_type=data['token_type'],
                        )
        

        return token

        
        


            
        


