from flask import Flask, jsonify
from authlib.flask.client import OAuth
import config
import os


oauth = OAuth()

oauth.register('google',
               client_id=os.getenv('Google_Client_ID'),
               client_secret=os.getenv('Google_Client_secret'),
               access_token_url='https://accounts.google.com/o/oauth2/token',
               access_token_params=None,
               refresh_token_url=None,
               authorize_url='https://accounts.google.com/o/oauth2/auth',
               api_base_url='https://www.googleapis.com/oauth2/v1/',
               client_kwargs={
                   'scope': 'profile',
                   'token_endpoint_auth_method': 'client_secret_basic',
                   'token_placement': 'header',
                   'prompt': 'consent'
               }
               )
