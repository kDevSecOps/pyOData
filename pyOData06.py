# 3.1.6 Dealing with errors during parsing metadata

'''
Class config provides easy to use wrapper for all parser configuration. These are:
• XML namespaces
• Parser policies (how parser act in case of invalid XML tag). We now support three types of policies:
– Policy fatal - the policy raises exception and terminates the parser
– Policy warning - the policy reports the detected problem, executes a fallback code and then continues
normally
– Policy ignore - the policy executes a fallback code without reporting the problem and then continues
normally
'''

import pyodata
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config
import requests

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

namespaces = {
    'edmx': 'customEdmxUrl.com',
    'edm': 'customEdmUrl.com'
}

custom_config = Config(
    xml_namespaces=namespaces,
    default_error_policy=PolicyFatal(),
    custom_error_policies={
        ParserError.ANNOTATION: PolicyWarning(),
        ParserError.ASSOCIATION: PolicyIgnore()
    })

northwind = pyodata.Client(SERVICE_URL, requests.Session(), config=custom_config)

print(northwind.schema.is_valid)