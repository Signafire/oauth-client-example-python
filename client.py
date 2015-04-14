from rauth import OAuth2Service
import json

# Fill in required access values
CLIENT_ID = "<CLIENT-ID>"
CLIENT_SECRET = "<CLIENT-SECRET>"
ACCESS_TOKEN_URL = "https://apis.signafire.com/token"

# Fill in required API values
API_NAME = "<API-NAME>"                         # eg. "chronolens"
API_VERSION = "<API-VERSION>"                   # eg. "v1"

# This is a basic test URL to test access to the API.
# See the API documentation for how to use specific endpoints
API_URL = "https://apis.signafire.com/%s/%s" % (API_NAME, API_VERSION)

# Creat the service
service = OAuth2Service(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        access_token_url=ACCESS_TOKEN_URL)

# Specify that we're using client credentials
data = {'grant_type': 'client_credentials'}

# Create the OAuth session
session = service.get_auth_session(data=data, decoder=json.loads)

# GET the test url to verify access
result = session.get(API_URL)
print(result.status_code)
print(result.json())
