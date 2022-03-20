# 3.2 Querying | 3.2.5 Get entities matching a filter in more Pythonic way

import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as esf

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

# Print unique identification (Id) of all employees with name John Smith:
# smith_employees_request = northwind.entity_sets.Employees.get_entities()
# smith_employees_request = smith_employees_request.filter(esf.and_(smith_employees_request.FirstName == 'Jonh', smith_employees_request.LastName == 'Smith'))
# for Smith in smith_employees_request.execute():
#     print(Smith.EmployeeID)

# Print unique identification (Id) of all employees with name Robert King:
robert_employees_request = northwind.entity_sets.Employees.get_entities()
robert_employees_request = robert_employees_request.filter(esf.and_(robert_employees_request.FirstName == 'Robert', robert_employees_request.LastName == 'King'))
for Robert in robert_employees_request.execute():
    print(Robert.EmployeeID)

