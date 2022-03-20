# 3.4 Updating


import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

'''To update an entity, you must create an updated request, set properties to the values you want and execute the request.
The library will send an HTTP PATCH request to the remote service.
'''

update_request = northwind.entity_sets.Customers.update_entity(CustomerID='ALFKI')
update_request.set(CompanyName='Alfons Kitten')
update_request.execute()

# pyodata.exceptions.HttpError: HTTP modify request for Entity Set Customers failed with status code 501
# 501(구현되지 않음): 서버에 요청을 수행할 수 있는 기능이 없다. 예를 들어 서버가 요청 메소드를 인식하지 못할 때 이 코드를 표시한다.