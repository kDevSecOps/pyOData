# 3.1.5 Get the service with local metadata

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

with open('/the/file/path.xml', 'rb') as mtd_file:
    local_metadata = mtd_file.read()

northwind = pyodata.Client(SERVICE_URL, requests.Session(), metadata=local_metadata)