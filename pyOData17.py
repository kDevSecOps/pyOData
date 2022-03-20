# 3.2 Querying | 3.2.7 Get entities matching a complex filter in ORM style

import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as esf

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

# Print unique identification (Id) of all employees with name Robert King:
robert_employees_request = northwind.entity_sets.Employees.get_entities()
robert_employees_request = robert_employees_request.filter(FirstName__contains = 'ob', LastName__contains = 'Ki')
for robert in robert_employees_request.execute():
    print(robert.EmployeeID)
