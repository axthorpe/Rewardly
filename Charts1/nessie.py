import requests
import json
import random
import math
from operator import itemgetter

def generateDates():
	transaction_year = 2010 + int(math.floor(random.random()*5))
	transaction_month = 1 + int(math.floor(random.random()*12))
	transaction_day = 1 + int(math.floor(random.random()*28))
	return (str(transaction_year) + str(transaction_month) + str(transaction_day))

def depAmounts():
	amount = 2000*random.random()
	return amount

def withAmounts():
	amount = 1000*random.random()
	return amount

def iterate():
	numTransactions = 1000
	numDeposits = numTransactions/2
	numWithdrawals = numTransactions/2

	depDates = [0] * numDeposits
	withDates = [0] * numWithdrawals
	depList = [0] * numDeposits
	withList = [0] * numWithdrawals
	
	for i in range(numDeposits):
		depDates[i] = generateDates()
	for i in range(numWithdrawals):
		withDates[i] = generateDates()

	#print depDates

	depDates = sorted(depDates, key=itemgetter(2,1,0))
	withDates = sorted(withDates, key=itemgetter(2,1,0))

	for i in range(numDeposits):
		depList[i] = [depDates[i], depAmounts()]
	
	for i in range(numWithdrawals):
		withList[i] = [withDates[i], withAmounts()]

	return depList, withList

def postAccount(cId, apiId):
	responseAction = {
		201 : lambda : print('It worked'),
		400 : lambda : print('Uh oh, something in your payload is wrong'),
	}
	 
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
	payload = {
	  "type": "Savings",
	  "nickname": "Test",
	  "rewards": 100,
	  "balance": 10000,	
	}
	 
	req = requests.post(
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)
	print (responseAction[req.status_code]())
 
def getAccounts():
	req = requests.get("http://api.reimaginebanking.com:8080/customers?key=319d9c6be999ebdfa861125ad5c5fef2");
	return (req.text)

def getAccounts(cId, apiId):
	req = requests.get('http://api.reimaginebanking.com:8080/customers/{}/accounts?key={}'.format(cId,apiId))
	return (req.text)

def deposit(accId, apiId):
	url = 'http://api.reimaginebanking.com:8080/accounts/{}/deposits?key={}'.format(accId,apiKey)
	payload = {

	  "medium": "balance",
	  "transaction_date": generateDates(),
	  "status": "completed",
	  "amount": int(depAmounts()),
	  "description": "Deposit"
	}
	req = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},)
	print (req.text)

def withdraw(accId, apiId):
	url = 'http://api.reimaginebanking.com:8080/accounts/{}/withdrawals?key={}'.format(accId,apiKey)
	payload = {
 		"medium": "balance",
		"amount": int(withAmounts()),
		"transaction_date": generateDates(),
		"status": "completed",
		"description": "Withdrawal"
}
	req = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},)
	print (req.text)

customerId = '555bed95a520e036e52b2104'
apiKey = '319d9c6be999ebdfa861125ad5c5fef2'
accId = '555e8364566c6e7c4d4d5655'

for _ in range(100):
	deposit(accId, apiKey)
	withdraw(accId,apiKey)


# postAccount(customerId, apiKey);

