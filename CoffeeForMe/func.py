#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: func.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	The functionality list to cover tool requirements
"""
from coffee import coffeeTeam, coffeeManager, coffeeBarista
import datetime
import logging

logging.basicConfig(filename='log/log.log',level=logging.DEBUG)

# drink options
DRINK_OPTION = {
	"sugar": 0.35,
	"cinnamon": 0.15,
	"milk": 0.50,
	"ice": 0.10,
	"pepper": 0.18}

# default drinks
"""
"Cappuccino": 2.99
"Latte": 1.99
"Mocha": 2.99
"Americano": 3.10
"Macchiato": 3.99
"""

def log(level, msg):
	date = datetime.datetime.now()
	dt = date.strftime("%H:%M:%S - %m/%d/%y")
	if level == "debug":
		logging.debug("{}: {}".format(dt,msg))
	elif level == "info":
		logging.info("{}: {}".format(dt,msg))
	elif level == "warning":
		logging.warning("{}: {}".format(dt,msg))
	elif level == "error":
		logging.error("{}: {}".format(dt,msg))
		

def show_manager_menu(session_user, session_role):
	# manager menu
	print """
	2 - Logout: {} ({})
	3 - Create a new report
	9 - Add a new drink
	0 - Exit
	""".format(session_user, session_role)
	log("info", "requested manager menu from {}".format(session_user))
	
def show_barista_menu(session_user, session_role):
	# barista menu
	print """
	2 - Logout: {} ({})
	4 - Make order
	0 - Exit
	""".format(session_user, session_role)
	log("info", "requested barista menu from {}".format(session_user))
	
def show_regular_menu():
	# non logged user menu
	print """
	1 - Add a new CoffeForMe team member
	2 - Login
	0 - Exit
	"""
	
def add_new_team_member():
	# create a new team member
	new_member = []
	user_input = raw_input("A new CoffeeForMe team member: manager or barista? ")
	if (user_input == "manager"):
		# ask all what we need
		new_member.append(user_input)
		user_input = raw_input("Please enter user name and password ")
		user_input = user_input.split()
		new_member.append(user_input[0])
		new_member.append(user_input[1])
		# create a new team member
		manager = coffeeTeam(new_member[1],new_member[0],new_member[2])
		if manager:
			log("info", "A new user is added: {}-{}-{}".format(new_member[1],new_member[0],new_member[2]))
	elif (user_input == "barista"):
		# ask all what we need
		new_member.append(user_input)
		user_input = raw_input("Please enter user name and password ")
		user_input = user_input.split()
		new_member.append(user_input[0])
		new_member.append(user_input[1])
		# create a new team member
		barista = coffeeTeam(new_member[1],new_member[0],new_member[2])
		if barista:
			log("info", "A new user is added: {}-{}-{}".format(new_member[1],new_member[0],new_member[2]))

def try_to_login(name=None, passwd=None):		
	# try to login
	data = False
	member = coffeeTeam()
	if (name == None) and (passwd == None):
		try:
			user_input = raw_input("Please enter user name and password ")
			user_input = user_input.split()
			res = member.get_member(user_input[0], user_input[1])
			if res:
				log("info", "logged as: {}".format(res[1]))
				data = res
			else:
				log("error", "failed to login with: {}-{}".format(user_input[0], user_input[1]))
		except IndexError as e:
			log("error", "failed to login: {}".format(e))
		
	if (name != None) and (passwd != None):
		res = member.get_member(name, passwd)
		if res:
			log("info", "logged as: {}".format(res[1]))
			data = res
		else:
			log("error", "failed to login with: {}-{}".format(name, passwd))
			
	return data		
		
def get_revenue_report():
	# get summary revenue table for manager
	log("info", "generated revenue menu")
	manager = coffeeManager()
	report = manager.get_revenue_report()						
	grand_total = 0
	print("____________________________________")
	print("Name	-	N of sales	-	Total value")
	for order in report:
		print("[{}] - {}	-	{}		-		${}".format(order[0], order[1], order[2], order[3]))
		grand_total += order[2]
	print("Grand Total: grand_total:	${}".format(grand_total))
	print("____________________________________")
	
def get_drinks():
	barista = coffeeBarista()
	drink_list = barista.get_drink_list()
	return drink_list
	
def save_order(session_id, drink_id=None, drink_options=None, seller_id=None):
	date = datetime.datetime.now()
	dt = date.strftime("%H:%M:%S - %m/%d/%y")
	# show the list of drinks and ask
	if drink_id != None and seller_id != None:
		# save drink from console (not interactivemode)
		# list drink_id
		barista = coffeeBarista()
		drink = barista.get_drink_list(drink_id)	
		# drink[2] = drink price from db
		drink_price = drink[0][2]
		# list drink_options
		if drink_options != None:
			# get the price of all drink options
			for option in drink_options:
				drink_price += DRINK_OPTION.values()[int(option)]
		# seller_id
		# make_order(self, date, price, seller_id, drink_id):
		result = barista.make_order(
			dt,
			drink_price,
			seller_id,
			drink[0][0]
		)
		if result:
			log("info", "A new order is saved from console {} price: {} | drink id: {}".format(seller_id, drink_price, drink[0][0]))
		
	else:
		barista = coffeeBarista()
		drink_list = barista.get_drink_list()
		drink_order = []
		if (drink_list == []):
			log("warnig", "The list of drinks is empty!")
		else:
			try:
				for key, drink in enumerate(drink_list):
					# id name price
					print "[{}] - {} (${})".format(key, drink[1], drink[2])
				user_drink = raw_input("Please select a drink ")
				if (int(user_drink) not in range(0,len(drink_list))):
					log("error", "Wrong drink index")
					
					
				else:
					# need to grab drink id name and price
					drink_order.append([
							drink_list[int(user_drink)][0],
							drink_list[int(user_drink)][1],
							drink_list[int(user_drink)][2]
							])
					
					# hold the selection and ask about additional drink options
					drink_order_options = []
					while True:
						print "Drink options | press q to exit"
						for  key, val in enumerate(DRINK_OPTION):
							print "[{}] - {} ({})".format(key, val, DRINK_OPTION[val])
						print "[q] - Exit"
						user_drink_options = raw_input("Please select extra options ")
						if (user_drink_options == "q"): break
						elif (int(user_drink_options) not in range(0,len(DRINK_OPTION))):
							log("error", "Wrong drink option index")
						else:	
							drink_order_options.append([DRINK_OPTION.keys()[int(user_drink_options)], DRINK_OPTION.values()[int(user_drink_options)]])
					drink_price = drink_order[0][2]
					if drink_order_options != []:
						for options_price in drink_order_options:
							drink_price += options_price[1]
					print("______________________________")
					print("The final price is: ${}".format(drink_price))
					print("")
					print("Drink details:")
					print(drink_order)
					print(drink_order_options)
					print("______________________________")
					# ask about save order?
					save_order = raw_input("Would you like to save order? (y|n) ")
					if (save_order == "y"): 
						# make_order(self, date, price, seller_id, drink_id):
						result = barista.make_order(
							dt,
							drink_price,
							session_id,
							drink_order[0][0]
						)
						if result:
							log("info", "A new order is saved from menu {} price: {} | drink id: {}".format(seller_id, drink_price, drink_order[0][0]))
			except ValueError as e:
				log("error", "Make order error, wrong params: {}".format(e))
					
def add_new_drink(name=None, price=None):
	# add a new drink into db
	try:
		if name == None and price == None:
			user_input = raw_input("Please enter a new drink and price ")
			# example: Latte 2.99
			user_input = user_input.split()
		else:
			user_input = []
			user_input.append(name)
			user_input.append(price)
		manager = coffeeManager()
		result = manager.add_drink(user_input[0], float(user_input[1]))
		if result:
			log("info", "A new drink is added: {} $({})".format(user_input[0], user_input[1]))
	except ValueError as e:
		print("Input error: {}".format(e))
		log("error", "Input error during adding new drink: {}".format(e)) 
		
def get_options():
	for  key, val in enumerate(DRINK_OPTION):
		print "[{}] - {} ({})".format(key, val, DRINK_OPTION[val])