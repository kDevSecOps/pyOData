# 3.1.7 Prevent substitution by default values

'''Per default, missing properties get filled in by type specific default values. While convenient, this throws away the
knowledge of whether a value was missing in the first place. To prevent this, the class config mentioned in the section
above takes an additional parameter, retain_null.'''

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

#northwind = pyodata.Client(SERVICE_URL, requests.Session(), config=pyodata.v2.model.Config(retain_null=True))
northwind = pyodata.Client(SERVICE_URL, requests.Session(), config=pyodata.v2.model.Config(retain_null=False))
# Changing retain_null to False will print Shipped date: 1753-01-01 00:00:00+00:00.

unknown_shipped_date = northwind.entity_sets.Orders_Qries.get_entity(OrderID=11058, CompanyName='Blauer See Delikatessen').execute()

print(
    f'Shipped date: {"unknown" if unknown_shipped_date.ShippedDate is None else unknown_shipped_date.ShippedDate}')