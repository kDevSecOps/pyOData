# Chap02 - Basic usage
#provide an object implementing interface compatible with Session from the library Requests

import pyodata
import requests
SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'
HTTP_LIB = requests.Session()

northwind = pyodata.Client(SERVICE_URL, HTTP_LIB)
for customer in northwind.entity_sets.Customers.get_entities().execute():
    print(customer.CustomerID, customer.CompanyName)