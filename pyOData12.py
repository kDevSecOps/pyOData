# 3.2 Querying | 3.2.2 Get one entity identified by its key value which is not scalar

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




# northwind = pyodata.Client(SERVICE_URL, requests.Session(), config=custom_config)# Get number of orderd units in the order identified by ProductID 42 and OrderID 10248:
northwind = pyodata.Client(SERVICE_URL, requests.Session())

# Get number of orderd units in the order identified by ProductID 42 and OrderID 10248:
order = northwind.entity_sets.Order_Details.get_entity(OrderID=10248, ProductID=42).execute()
print(order.Quantity)