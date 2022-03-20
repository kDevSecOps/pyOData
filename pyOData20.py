# 3.3 Creating

'''The create action executes the HTTP method POST which is usually protected by CSRF and therefore you must make
some effort to initialize your HTTP Session to send POST requests acceptable by the remote server.
'''

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'
# SERVICE_URL = 'http://example.io/TheServiceRoot/'

session = requests.Session()
response = session.head(SERVICE_URL, headers={'x-csrf-token': 'fetch'})
token = response.headers.get('x-csrf-token', '')
session.headers.update({'x-csrf-token': token})

theservice = pyodata.Client(SERVICE_URL, session)