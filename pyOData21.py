# 3.3 Creating | 3.3.1 Create an entity with a complex type property

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'
# SERVICE_URL = 'http://example.io/TheServiceRoot/'

# session = requests.Session()
# response = session.head(SERVICE_URL, headers={'x-csrf-token': 'fetch'})
# token = response.headers.get('x-csrf-token', '')
# session.headers.update({'x-csrf-token': token})

# theservice = pyodata.Client(SERVICE_URL, session)

northwind = pyodata.Client(SERVICE_URL, requests.Session())

employee_data = {
    'FirstName': 'Mark',
    'LastName': 'Goody',
    'Address': {
        'HouseNumber': 42,
        'Street': 'Paradise',
        'City': 'Heaven'
    }
}

create_request = northwind.entity_sets.Employees.create_entity()
create_request.set(**employee_data)

new_employee_entity = create_request.execute()


# count = northwind.entity_sets.Employees.get_entities().count().execute()
# # print(count)
# print("Number of Employees:", count)