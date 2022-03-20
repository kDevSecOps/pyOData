# 3.2 Querying | 3.2.4 Get entities matching a filter

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

employees = northwind.entity_sets.Employees.get_entities().select('EmployeeID,LastName').execute()

# Print unique identification (Id) of all employees with name John Smith:
smith_employees_request = northwind.entity_sets.Employees.get_entities()

smith_employees_request = smith_employees_request.filter("FirstName eq 'John' and LastName eq 'Smith'")

for smith in smith_employees_request.execute():
    print(smith.EmployeeID)