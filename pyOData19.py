# 3.2 Querying | 3.2.9 Get a count of entities via navigation property

import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as esf

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

# Print a count of all orders associated with Employee 1:
count = northwind.entity_sets.Employees.get_entity(1).nav('Orders').get_entities().count().execute()
print(count)

# Print all orders associated with Employee 1 and their count:
orders = northwind.entity_sets.Employees.get_entity(1).nav('Orders').get_entities().count(inline=True).execute()
print("total_count:", orders.total_count)
for order in orders:
    print("Order ID: ",order.OrderID, "Product ID:", order.ProductID)