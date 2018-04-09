#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: func.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	A lot of def to hide the main routine
"""
from coffee import coffeeTeam, coffeeManager, coffeeBarista
import datetime

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

def show_manager_menu(session_user, session_role):
	print """
	2 - Logout: {} ({})
	3 - Create a new report
	9 - Add a new drink
	0 - Exit
	""".format(session_user, session_role)
	
def show_barista_menu(session_user, session_role):
	print """
	2 - Logout: {} ({})
	4 - Make order
	0 - Exit
	""".format(session_user, session_role)
	
def show_regular_menu():
	print """
	1 - Add a new CoffeForMe team member
	2 - Login
	0 - Exit
	"""
	
def add_new_team_member():
	new_member = []
	user_input = raw_input("Let's add a new CoffeeForMe team member: [manager|barista]? ")
	if (user_input == "manager"):
		# ask all what we need
		new_member.append(user_input)
		user_input = raw_input("Please enter user name and password ")
		user_input = user_input.split()
		new_member.append(user_input[0])
		new_member.append(user_input[1])
		# create a new team member
		barista = coffeeTeam(new_member[1],new_member[0],new_member[2])
	elif (user_input == "barista"):
		# ask all what we need
		new_member.append(user_input)
		user_input = raw_input("Please enter user name and password ")
		user_input = user_input.split()
		new_member.append(user_input[0])
		new_member.append(user_input[1])
		# create a new team member
		manager = coffeeTeam(new_member[1],new_member[0],new_member[2])

def try_to_login():		
	# try to login
	user_input = raw_input("Please enter user name and password ")
	user_input = user_input.split()
	member = coffeeTeam()
	res = member.get_member(user_input[0], user_input[1])
	
	if (res):
		return (res[0],res[1],res[2])
	else:
		return False
	
def get_revenue_report():
	manager = coffeeManager()
	report = manager.get_revenue_report()						
	grand_total = 0
	print("____________________________________")
	print("Name	-	N of sales	-	Total value")
	for order in report:
		print("{}	-	{}		-		${}".format(order[0], order[1], order[2]))
		grand_total += order[2]
	print("Grand Total: grand_total:	${}".format(grand_total))
	print("____________________________________")
	
def save_order(session_id):
	# show the list of drinks and ask
	barista = coffeeBarista()
	drink_list = barista.get_drink_list()
	drink_order = []
	if (drink_list == []):
		print "The list of drinks is empty!"
	else:
		for key, drink in enumerate(drink_list):
			# id name price
			print "[{}] - {} (${})".format(key, drink[1], drink[2])
		user_drink = raw_input("Please select a drink ")
		
		# need to grab drink id name and price
		drink_order.append([
				drink_list[int(user_drink)][0],
				drink_list[int(user_drink)][1],
				drink_list[int(user_drink)][2]
				])
		
		# hold the selection and ask about additional drink options
		drink_order_options = []
		while True:
			print "Drink options | press 0 to exit"
			for  key, val in enumerate(DRINK_OPTION):
				print "[{}] - {} ({})".format(key, val, DRINK_OPTION[val])
				
			print "[q] - Exit"
			user_drink_options = raw_input("Please select extra options ")
			
			if (user_drink_options == "q"): break
			else:
				drink_order_options.append([DRINK_OPTION.keys()[int(user_drink_options)], DRINK_OPTION.values()[int(user_drink_options)]])
	
		drink_price = drink_order[0][2]
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
			date = datetime.datetime.now()
			dt = date.strftime("%H:%M:%S - %m/%d/%y")
			# make_order(self, date, price, seller_id, drink_id):
			barista.make_order(
				dt,
				drink_price,
				session_id,
				drink_order[0][0]
			)
def add_new_drink():
	user_input = raw_input("Please enter a new drink and price ")
	# example: Latte 2.99
	user_input = user_input.split()
	manager = coffeeManager()
	manager.add_drink(user_input[0], float(user_input[1]))

			
			
	
	