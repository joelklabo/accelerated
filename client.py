import json
import time
import subprocess

# Import from 21 developer library
import two1.commands.status
from two1.lib.server import rest_client
from two1.commands.config import TWO1_HOST
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

SERVER_URL = 'http://localhost:5003/fastfind'

# Set up wallet proxy
wallet = Wallet()

# Read local user account data
config = Config()
username = Config().username

# Initialize rest client to communicate with 21.co API
client = rest_client.TwentyOneRestClient(TWO1_HOST, config.machine_auth, config.username)

# Set up bitrequests client using BriTransfer payment method for 402 requests
requests = BitTransferRequests(wallet, username)

# Check the spot price for our API call
response = requests.get_402_info(url=SERVER_URL)
endpoint_info = dict(response)
price = int(endpoint_info['price'])

def get_element(arr, prop, val):
  for elem in arr:
    if elem[prop] == val:
      return val
    time.sleep(1)

# fast bitcoin aware api NOx
def fast_get_element(arr, prop, val):
  body = {
    'array': json.dumps(arr),
    'property': prop,
    'value': val
  }
  res = requests.post(url=SERVER_URL, data=body)
  return json.loads(res.text)['elem']

# Sample data
data1 = [
  {'height': 4},
  {'height': 3},
  {'height': 6},
  {'height': 4},
  {'height': 3},
  {'height': 6},
  {'height': 4},
  {'height': 4},
  {'height': 3},
  {'height': 6},
  {'height': 10}
]

t0 = time.time()
a = get_element(data1, 'height', 10)
t1 = time.time()

# Print results
print(a)
print("Execution time: " + str(t1-t0))
