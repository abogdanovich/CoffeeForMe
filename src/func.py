#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: func.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	The functionality list to cover tool requirements
"""
from coffee import coffeeTeam
import datetime
import logging
from prettytable import PrettyTable
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename="{}/log/log.log".format(current_dir),level=logging.DEBUG)

# drink options
DRINK_OPTION = {
	"sugar": 0.35,
	"cinnamon": 0.15,
	"milk": 0.50,
	"ice": 0.10,
	"pepper": 0.18}

# default drinks
DEFAULT_DRINK = {
	"Cappuccino": 2.99,
	"Latte": 1.99,
	"Mocha": 2.99,
	"Americano": 3.10,
	"Macchiato": 3.99
}

def log(level, msg):
	# make sure that we're logging everyone 
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
		
def show_menu():
	# manager menu
	x = PrettyTable()
	x.field_names = ["Item", "Description"]
	x.add_row(["1","Add a new user"])
	x.add_row(["2","Login"])
	x.add_row(["0","Exit"])
	x.align = "l"
	print(x)
	
def show_menu_manager(user):
	# manager menu
	x = PrettyTable()
	x.field_names = ["Item", "Description"]		
	if (user):
		if user.role == "manager":
			x.add_row(["2","Logout: {} ({})".format(user.name, user.role)])
			x.add_row(["3","Revenue report"])
			x.add_row(["9","Add a new drink"])
	x.add_row(["0","Exit"])
	x.align = "l"
	print(x)
	
def show_menu_barista(user):
	# barista menu
	x = PrettyTable()
	x.field_names = ["Item", "Description"]		
	if (user):
		if user.role == "barista":
			x.add_row(["2","Logout: {} ({})".format(user.name, user.role)])
			x.add_row(["4","Make order"])
	x.add_row(["0","Exit"])
	x.align = "l"
	print(x)	
		
def add_new_team_member(**kwargs):
	# create a new team member
	user = None
	try:
		if len(kwargs) >= 3:
			new_user = {"role": kwargs["role"], "name": kwargs["name"], "passwd": kwargs["passwd"]}		
		else:
			# ask if no input params
			user_input = raw_input("Enter a new CoffeeForMe team member like: `manager Alex passwd` ")
			if len(user_input.split()) >= 3:
				new_user = {"role": user_input.split()[0], "name": user_input.split()[1], "passwd": user_input.split()[2]}
				user = coffeeTeam(**new_user)
				if user.logged:
						log("info", "A new user is added: {}-{}".format(user.name, user.role))
						print("info", "A new user is added: {}-{}".format(user.name, user.role))
			else:
				log("error", "failed to add: not anough params")
	except IndexError as e:
			log("error", "failed to login: {}".format(e))
	return user	

def make_login(**kwargs):		
	# try to login
	user = None
	user_params = None
	try:
		if (len(kwargs) >= 2):
			user_params = {"name": kwargs["name"], "passwd": kwargs["passwd"]}
		else:
			user_input = raw_input("Please enter user name password ")
			if len(user_input.split()) >= 2:
				user_params = {"name": user_input.split()[0], "passwd": user_input.split()[1]}
			
		if user_params is not None:
			user = coffeeTeam(**user_params)
			if user.logged:
				log("info", "logged as: {}".format(user.name))
			else:
				log("error", "failed to login with: {}-{}".format(user_input[0], user_input[1]))
	except IndexError as e:
			log("error", "failed to login: {}".format(e))
	return user		
		
def get_revenue_report(user):
	# get the revenue report
	grand_total = 0
	x = PrettyTable()
	# get summary revenue table for manager
	log("info", "generated revenue menu")
	# call static class method (no relation with class data)
	data = user.get_revenue_data()
	if data:
		grand_total = 0
		x.field_names = ["Barman", "Number os sales", "Total $"]
		for order in data:
			x.add_row([order[1], order[2], order[3]])
			grand_total += order[3]
		x.align = "l"
		print(x)
		print "GRAND TOTAL: ${}".format(grand_total)
	return grand_total

def show_options():
	# show drik options
	x = PrettyTable()
	x.field_names = ["ID", "Option", "Price"]
	for  key, val in enumerate(DRINK_OPTION):
		x.add_row([key, val, DRINK_OPTION[val]])
	x.align = "l"
	print(x)
		
def show_drinks(user):
	# show the list of all drinks
	drink_list = user.get_drink_list()
	x = PrettyTable()
	x.field_names = ["ID", "Drink", "Price"]					
	for key, drink in enumerate(drink_list):
		# id name price
		x.add_row([key, drink[1], drink[2]])
	x.align = "l"
	print(x)
	
def save_order(user, **kwargs):
	# save order into db
	try:
		# session_role, session_id, drink_id=None, drink_options=None, seller_id=None
		date = datetime.datetime.now()
		dt = date.strftime("%H:%M:%S - %m/%d/%y")
		# show the list of drinks and ask
		if "drink_id" in kwargs:
			order = {"barista": user.uid, "datetime": dt, "price": kwargs["price"], "drink_id": kwargs["drink_id"]}
		else:
			order = None
			# call static method
			drink_list = user.get_drink_list()
			print drink_list
			drink_order = []
			if (drink_list == []):
				log("warnig", "The list of drinks is empty!")
			else:
				# show the list of all available drinks
				show_drinks(user)
				user_drink = raw_input("Please select a drink ")
				print user_drink
				if (int(user_drink) not in range(0,len(drink_list))):
					log("error", "Wrong drink index")
				else:
					print user_drink
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
						show_options()
						print "[q] - Exit"
						user_drink_options = raw_input("Please select extra options ")
						if (user_drink_options == "q"): break
						elif (int(user_drink_options) not in range(0,len(DRINK_OPTION))):
							log("error", "Wrong drink option index")
						else:	
							drink_order_options.append([DRINK_OPTION.keys()[int(user_drink_options)], DRINK_OPTION.values()[int(user_drink_options)]])
					# calc the drink with options price
					drink_price = drink_order[0][2]
					if drink_order_options != []:
						for options_price in drink_order_options:
							drink_price += options_price[1]
					x = PrettyTable()
					x.field_names = ["Drink", "Options", "Price"]
					x.add_row([drink_order, drink_order_options, drink_price])
					x.align = "l"
					print(x)
					
					# ask about save order?
					ask_save_order = raw_input("Would you like to save order? (y|n) ")
					if ask_save_order == "y":
						order = {"barista": user.uid, "datetime": dt, "price": drink_price, "drink_id": user_drink}

		if order is not None:
			result = user.save_order(**order)
			if result:
				log("info", "A new order is saved from ")					
	except ValueError as e:
		log("error", "Make order error, wrong params: {}".format(e))
	return result
					
def add_new_drink(user, **kwargs):
	# add a new drink into db
	try:
		if len(kwargs) >= 2:
			drink = {"name": kwargs["name"], "price": kwargs["price"]}			
		else:
			# example: Latte 2.99
			user_input = raw_input("Please enter a new drink and price ")
			drink = {"name": user_input.split()[0], "price": user_input.split()[1]}
		data = user.save_drink(**drink)
		if data:
			log("info", "A new drink is added: {} $({})".format(drink["name"], drink["price"]))
	except ValueError as e:
		log("error", "Input error during adding new drink: {}".format(e))
	return data