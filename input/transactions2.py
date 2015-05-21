import random
import math
from operator import itemgetter

def generateDates():

	transaction_year = 2010 + int(math.floor(random.random()*5))
	transaction_month = 1 + int(math.floor(random.random()*12))
	transaction_date = 1 + int(math.floor(random.random()*28))
	return (transaction_date, transaction_month, transaction_year)

def depAmounts():
	amount = 1000*random.random()
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