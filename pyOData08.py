# 3.1.8 Set custom namespaces (Deprecated - use config instead)

'''Let’s assume you need to work with a service which uses namespaces not directly supported by this library e. g. ones
hosted on private urls such as customEdmxUrl.com and customEdmUrl.com:'''

import pyodata
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

namespaces = {
    'edmx': 'customEdmxUrl.com',
    'edm': 'customEdmUrl.com'
}

northwind = pyodata.Client(SERVICE_URL, requests.Session(), namespaces=namespaces)