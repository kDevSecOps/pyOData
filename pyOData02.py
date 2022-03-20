# 3.1.2 Get the service proxy client for an OData service requiring sap-client parameter

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

session = requests.Session()
param = {'sap-client': '510'}
session.params = param
northwind = pyodata.Client(SERVICE_URL, session)