# 3.1.4 Get the service proxy client for an OData service requiring Certificate authentication

''' your service requires certificate based authentication and you are able to export the certificate into the file mycert.p12. 
You need to split the certificate into public key, private key and certificate authority key.

The following steps has been verified on Fedora Linux and Mac OS.
openssl pkcs12 -in mycert.p12 -out ca.pem -cacerts -nokeys
openssl pkcs12 -in mycert.p12 -out client.pem -clcerts -nokeys
openssl pkcs12 -in mycert.p12 -out key.pem -nocerts
openssl rsa -in key.pem -out key_decrypt.pem

You can verify your steps by curl:
curl --key key_decrypt.pem --cacert ca.pem --cert client.pem -k 'SERVICE_URL/$metadata
˓→'

For more information on client side SSL cerificationcas, please refer to this [gist](https://gist.github.com/mtigas/952344).

'''

import pyodata
import requests

SERVICE_URL = 'https://odata.example.com/Secret.svc'

session = requests.Session()
session.verify = 'ca.pem'
session.cert = ('client.pem', 'key_decrypt.pem')

client = pyodata.Client(SERVICE_URL, session)
