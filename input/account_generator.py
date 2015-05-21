import urllib2
import requests
import json
from accounts import generate

def generate_accounts(n):
	for account in [generate() for _ in range(n)]:
		req = requests.post('http://api.reimaginebanking.com/customers/{}/accounts?key=a77bdeec7637667dd4dd50c006e92c38'.format(account[0]), data=json.dumps(account[1]))
generate_accounts(5)