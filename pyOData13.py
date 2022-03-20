# 3.2 Querying | 3.2.3 Get all entities of an entity set

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

employees = northwind.entity_sets.Employees.get_entities().select('EmployeeID,LastName').execute()

# Print unique identification (Id) and last name of all employees:
for employee in employees:
    print(employee.EmployeeID, employee.LastName)
    # print(employee.EmployeeID, employee.FirstName, employee.LastName)