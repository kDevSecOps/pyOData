# 3.2 Querying | 3.2.8 Get a count of entities

import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as esf

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

# Print a count of all employees:
count = northwind.entity_sets.Employees.get_entities().count().execute()
# print(count)
print("Number of Employees:", count)

# Print all employees and their count:
employees = northwind.entity_sets.Employees.get_entities().count(inline=True).execute()
print("total_count:", employees.total_count)

for employee in employees:
    print(employee.EmployeeID, employee.LastName)