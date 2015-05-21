import random
import math

def generate():
	temp = range(16)
	temp2 = [0]*16
	for i in range(16):
		temp2[i] = hex(temp[i])
		temp2[i] = temp2[i][2:]

	idStr = ""
	for _ in range(24):
		idStr += random.choice(temp2)

	# idStr is the id

	typeList = ["Checking", "Savings", "Credit Card"]
	typeStr = random.choice(typeList)

	# typeStr is the type

	rewards = 1000*random.random()

	# rewards

	balance = 10000*random.random()

	# balance

	numBills = int(math.floor(random.random()*10))
	bill_ids = [""] * numBills
	for i in range(numBills):
		for _ in range(24):
			bill_ids[i] += random.choice(temp2)

	# bill_ids

	customer_id = ""
	for _ in range(24):
		customer_id += random.choice(temp2)

	# customer_id

	account = dict()

	word = ['']*4000
	k = 0
	with open("names.txt", "r") as f:
		f.read(1)
		for line in f:
			for char in line:
				if char == ' ':
					break
				word[k] += char
			k += 1
	accountNum = int(math.floor(random.random()*4000))
	nickname = word[accountNum] + "'s account"
	
	account["_id"] = idStr
	account["type"] = typeStr
	account["nickname"] = nickname
	account["rewards"] = rewards
	account["balance"] = balance
	account["bill_ids"] = bill_ids
	account["customer_id"] = customer_id
	account["nickname"] = nickname

	innerAccountsHash = dict()
	innerAccountsHash["type"] = typeStr
	innerAccountsHash["nickname"] = nickname	
	innerAccountsHash["rewards"] = rewards
	innerAccountsHash["balance"] = balance
	outerAccountsHash = dict()
	outerAccountsHash["customerId"] = innerAccountsHash

	return (account, outerAccountsHash)

def listAccounts():
	#accountList = list()
	#for i in range(5000):
#		accountList += account()

	accountList = generate()
	print accountList[0] #change this line; use as u want
	print accountList[1] #change this line; use as u want
	return accountList

listAccounts()