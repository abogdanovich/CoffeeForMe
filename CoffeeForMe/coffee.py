#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Date created:	4/19/2018
	Python Version: 2.7
	Project classes are placed here.
	
"""

class coffeeTeam(object):
	""" Base class """	
	def __init__(self, name, role):
		""" save team member with his name and company role into db """
		#roles: manager, barman
		self.name = name
		self.role = role
		pass
	def get_member(self):
		""" get the list of all team members """
		return self.name, self.role
	def remove_member(self):
		""" remove employee from DB """
		pass
	
class coffeeManager(coffeeTeam):
	""" Manager class with appropriate functions """
	def get_revenue_report(self):
		""" generate Manager revenue report in summary table """
		pass
	
class coffeeBarista(coffeeTeam):
	""" Manager class with appropriate functions """
	def get_drink_price(self, drink_id):
		""" return drink price """
		pass
	def make_order(self, date, count, price, seller_id, drink_id):
		""" make order and save it into DB """
		pass
	
class coffeeBar(object):
	""" Base Bar class to work with DB"""
	def __init__(self, name, price, options):
		""" base init class to add a new drink into DB """
		#save drink into db
		self.name = name
		self.price = price
		self.options = options
		pass
	def remove_drink(self, drink_id):
		""" remove a drink from DB """
		pass
	def get_drink_list(self):
		""" get the list of all saved drinks in DB """
		pass
	def update_drink(self, drink_id, name, price, options):
		""" update drink with a fresh data """
		pass
	