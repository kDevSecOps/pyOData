# 3.1.3 Get the service proxy client for an OData service requiring authentication

import pyodata
import requests

SERVICE_URL = 'https://odata.example.com/Secret.svc'

session = requests.Session()
session.auth = ('MyUser', 'MyPassword')

theservice = pyodata.Client(SERVICE_URL, session)