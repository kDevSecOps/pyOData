# 3.2 Querying | 3.2.1 Get one entity identified by its key value

import pyodata
# from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

# namespaces = {
#     'edmx': 'customEdmxUrl.com',
#     'edm': 'customEdmUrl.com'
# }

# custom_config = Config(
#     xml_namespaces=namespaces,
#     default_error_policy=PolicyFatal(),
#     custom_error_policies={
#         ParserError.ANNOTATION: PolicyWarning(),
#         ParserError.ASSOCIATION: PolicyIgnore()
#     })

# northwind = pyodata.Client(SERVICE_URL, requests.Session(), config=custom_config)
northwind = pyodata.Client(SERVICE_URL, requests.Session())

employee1 = northwind.entity_sets.Employees.get_entity(1).execute()
print(employee1.FirstName)