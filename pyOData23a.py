# 3.5 Deleting

'''The delete action executes the HTTP method DELETE which is usually protected by CSRF and therefore you must
make some effort to initialize your HTTP Session to send DELETE requests acceptable by the remote server.
'''

import pyodata
import requests

SERVICE_URL = 'http://example.io/TheServiceRoot/'

# session = requests.Session()
# response = session.head(SERVICE_URL, headers={'x-csrf-token': 'fetch'})
# token = response.headers.get('x-csrf-token', '')
# session.headers.update({'x-csrf-token': token})

# theservice = pyodata.Client(SERVICE_URL, session)
# # Failed to establish a new connection: [Errno 11001] getaddrinfo failed')

# You can either delete entity by passing its PropertyRef value to the delete function
request = service.entity_sets.Employees.delete_entity(23)
request.execute()