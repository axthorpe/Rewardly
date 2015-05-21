import datetime
import math
import Queue as Q
from transactions2 import iterate, withAmounts, depAmounts, generateDates

class Customer:
	"""A Customer has friends, deposits, and withdrawals, and can earn rewards accordingly"""

	MAX_BONUS = 0.05
	PERCENT_SCALE = 100
	NORMALIZE_FACTOR = 40
	SIZE_BONUS_SCALE = 1000

	def __init__(self, group, deposit_history=[], withdrawal_history=[]):
		"""Creates a Customer with friends and an optional initial deposit/withdrawal history"""
		self.deposit_history = deposit_history
		self.withdrawal_history = withdrawal_history
		self.balance = sum([deposit_history[i][1] for i in range(len(deposit_history))]) - sum([withdrawal_history[i][1] for i in range(len(withdrawal_history))])
		self.percent_growth = 0
		self.gross_growth = 0
		self.group = group # An array of other Customers
		group.add(self)

	def add_withdrawal(self, withdrawal):
		"""Adds a withdrawal to the cached history of customer withdrawals"""
		self.withdrawal_history.append(withdrawal)
		self.balance -= withdrawal[1]

	def add_deposit(self, deposit):
		"""Adds a deposit to the cached history of customer deposits"""
		self.deposit_history.append(deposit)
		self.balance += deposit[1]

	def compute_base_reward(self):
		"""Computes reward solely on deposit/withdrawal history"""
		monthly_average_deposits, deposits_last_month, monthly_average_withdrawals, withdrawals_last_month = self.compute_average_deposits(), self.deposits_last_month(), self.compute_average_withdrawals(), self.withdrawals_last_month()
		percent_growth = (deposits_last_month - withdrawals_last_month)/(monthly_average_deposits - monthly_average_withdrawals) - 1
		gross_growth = (deposits_last_month - withdrawals_last_month) - (self.compute_average_deposits(2) - self.compute_average_withdrawals(2))
		self.percent_growth, self.gross_growth = percent_growth, gross_growth
		if percent_growth <= 0:
			return 0
		return max(0, min(self.MAX_BONUS + math.log(percent_growth, self.NORMALIZE_FACTOR)/self.PERCENT_SCALE, percent_growth/100))

	def compute_group_bonus(self):
		"""Computes bonus reward based on comparisons with others in given group"""
		rank_list = self.group.rank_list()
		rank, group_size = rank_list.index(self) + 1, len(rank_list)
		return min(self.MAX_BONUS + math.log(group_size, 10)/self.SIZE_BONUS_SCALE, ((1 - rank/group_size)/self.NORMALIZE_FACTOR)*(1 + group_size/self.SIZE_BONUS_SCALE))
		
	def compute_net_bonus(self):
		"""Computes reward based on withdrawal/deposit history summed with reward from
		   outsaving peers in group"""
		if self.group:
			return self.compute_group_bonus() + self.compute_base_reward()
		return self.compute_base_reward()

	def leave_group(self):
		"""Removes this Customer from his/her current group"""
		if self.group:
			group.remove(self)
			self.group = None

	def join_group(self, group):
		"""Adds this customer to given group"""
		leave_group()
		group.add(self)
		self.group = group

	def compute_average_deposits(self, n=12):
		"""Computes average monthly deposited amount in the last n months"""
		start_date = [28, 12, 2014]
		start_date[1] -= 1 #set start_date to one month before current date for computation

		total = 0
		end_date = list(start_date)
		end_date[1] -= n
		while (end_date[1] <= 0):
			end_date[1] += 12
			end_date[2] -= 1
		for deposit in self.deposit_history:
			if (deposit[0][2] >= end_date[2] and deposit[0][2] <= start_date[2]):
				if deposit[0][2] == end_date[2]:
					if deposit[0][1] < end_date[1]:
						continue
					elif deposit[0][1] == end_date[1]:
						if deposit[0][0] < end_date[0]:
							continue
				elif deposit[0][2] == start_date[2]:
					if deposit[0][1] > start_date[1]:
						continue
					elif deposit[0][1] == start_date[1]:
						if deposit[0][0] > start_date[0]:
							continue
				total += deposit[1]
		return total/n

	def deposits_last_month(self):
		"""Returns total amount deposited in the last month"""
		start_date = [28, 12, 2014]

		total = 0
		for deposit in self.deposit_history:
			if start_date[1] == 1:
				if (start_date[1] == 12 and start_date[0] < deposit[0][0] and start_date[2] == deposit[0][2] + 1) or (start_date[1] == deposit[1] and start_date[0] >= deposit[0][0] and start_date[2] == deposit[0][2]):
					total += deposit[1]
			elif start_date[2] == deposit[0][2]:
				if (start_date[1] - 1 == deposit[0][1] and start_date[0] <= deposit[0][0]) or (start_date[1] == deposit[0][1] and start_date[0] >= deposit[0][0]):
					total += deposit[1]
		return total

	def compute_average_withdrawals(self, n=12):
		"""Returns average montly withdrawn amount in the last n months"""
		tmp = self.deposit_history
		self.deposit_history = self.withdrawal_history
		average_withdrawals = self.compute_average_deposits()
		self.deposit_history = tmp
		return average_withdrawals

	def withdrawals_last_month(self):
		"""Returns total amount withdrawn in the last month"""
		tmp = self.deposit_history
		self.deposit_history = self.withdrawal_history
		withdrawals_last_month = self.deposits_last_month()
		self.deposit_history = tmp
		return withdrawals_last_month

	def add_bonus(self):
		"""Updates balance to reflect rewards bonus"""
		gross_growth = ((self.deposits_last_month() - self.withdrawals_last_month()) - (self.compute_average_deposits(2) - self.compute_average_withdrawals(2)))
		if gross_growth > 0:
			self.balance += gross_growth * self.compute_net_bonus()

	def __cmp__(self, other):
		"""Compares this Customer's performance to performance of other Customer"""
		if self.percent_growth != other.percent_growth:
			return cmp(self.percent_growth, other.percent_growth)
		return cmp(self.gross_growth, other.gross_growth)


class Group:
	"""A Group has members, who are competing with one another for reward bonuses"""
	
	def __init__(self):
		"""Creates a Group with a list of members"""
		self.q = []

	def add(self, new_member):
		"""Adds a new member to this group"""
		self.q.append(new_member)
		self.q = sorted(self.q)

	def remove(self, member):
		"""Removes given member from this group"""
		self.q.remove(member)

	def rank_list(self):
		return self.q

test_group = Group()
for _ in range(100):
	deposit_history, withdrawal_history = iterate()
	test_customer = Customer(test_group, deposit_history, withdrawal_history)
	print "INITIAL BALANCE: " + str(test_customer.balance)
	print "BONUS: " + str(test_customer.compute_net_bonus())
	print "RANK: " + str(test_customer.group.rank_list().index(test_customer) + 1)
	print "GROSS GROWTH: " + str(test_customer.gross_growth)
	test_customer.add_bonus()
	print "FINAL BALANCE: " + str(test_customer.balance)
	print
