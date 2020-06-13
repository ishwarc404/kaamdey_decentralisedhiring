#this script will help search and filter though the database

import requests
import json
import functions 



def individualSearch(address,profession):
    response = requests.get(f'http://localhost:3000/data?sponsor_individualaddress={address}&sponsor_individualprofession={profession}')