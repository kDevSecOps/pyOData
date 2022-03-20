# 3.2 Querying | 3.2.10 Use non-standard OData URL Query parameters

import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as esf

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

''' Sometimes services implement extension to OData model and require addition URL query parameters. In such a case,
you can enrich HTTP request made by pyodata with these parameters by the method custom(name: str, value: str).
'''
employee = northwind.entity_sets.Employees.get_entity(1).custom('sap-client', '100').execute()

count = northwind.entity_sets.Employees.get_entity(1).custom('sap-client', '100').nav('Orders').get_entities().count().execute()
print(count)
