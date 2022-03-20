# 3.4 Updating


import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

'''In the case the service you are dealing with requires PUT method, you have two options.
The first option allows you to change the used HTTP method for a single call via the key word parameter method of
the method update_entity.
'''

update_request = northwind.entity_sets.Customers.update_entity(CustomerID='ALFKI', method='PUT')
update_request.set(CompanyName='Alfons Kitten')
update_request.execute()

# pyodata.exceptions.HttpError: HTTP modify request for Entity Set Customers failed with status code 403
# 403(Forbidden, 금지됨): 서버가 요청을 거부하고 있다. 예를 들자면, 사용자가 리소스에 대한 필요 권한을 갖고 있지 않다. (401은 인증 실패, 403은 인가 실패라고 볼 수 있음)