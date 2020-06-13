#this script will help search and filter though the database

import requests
import json
import functions 


def individualSearch(profession,address):
    response = requests.get(f'http://localhost:3000/data?sponsor_individualaddress={address}&sponsor_individualprofession={profession}')
    results  = json.loads(response.content)
    return results

