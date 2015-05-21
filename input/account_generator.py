import urllib2
import requests
import json
from accounts import generate
from deposits import generate2

def generate_accounts(n):
	for account in [generate() for _ in range(n)]:
		req = requests.post('http://api.reimaginebanking.com/customers/{}/accounts?key=a77bdeec7637667dd4dd50c006e92c38'.format(account[0]), data=json.dumps(account[1]))
def generate_deposits(n):
	for account in [generate2() for _ in range(n)]:
		req = requests.post('http://api.reimaginebanking.com/accounts/{}/deposits?key=a77bdeec7637667dd4dd50c006e92c38'.format(account[0]), data=json.dumps(accounts[1]))
generate_accounts(1000)
generate_deposits(1000)