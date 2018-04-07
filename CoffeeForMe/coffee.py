#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Project classes are placed here.
"""

import sqlite3

class coffeeTeam(object):
	"""Base class"""	
	def __init__(self, name=None, role=None, db="db.db"):
		"""save team member with his name and company role into db"""
		
		self.name = name
		self.role = role
		self.db = db
		if (name is not None):
			self.add_member()
		
	def get_members(self):
		"""get the list of all team members"""
		
		connection = sqlite3.connect(self.db)
		with connection:
			result = connection.execute("SELECT * FROM team")
			data = result.fetchall()
			#print "added a new member: id {}".format(data[0])
			return data
			
		
	def remove_member(self):
		"""remove employee from DB"""
		
		pass
	def add_member(self):
		connection = sqlite3.connect(self.db)
		with connection:
			connection.execute('''CREATE TABLE IF NOT EXISTS team (
							   id INTEGER PRIMARY KEY AUTOINCREMENT,
							   name TEXT,
							   role TEXT
							   )''')
			
			if (self.role is None):
				self.role = 'unknown'
			connection.execute("INSERT INTO team (name, role) VALUES (?,?)", (self.name, self.role))
			result = connection.execute("SELECT last_insert_rowid()")
			data = result.fetchone()
			print "added a new member: id {}".format(data[0])
	
class coffeeManager(coffeeTeam):
	"""Manager class with appropriate functions"""
	def get_revenue_report(self):
		"""generate Manager revenue report in summary table"""
		
		pass
	def get_members(self, role="manager"):
		"""get the list of all Managers"""
		
		connection = sqlite3.connect(self.db)
		with connection:
			result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
			data = result.fetchall()
			return data
	
class coffeeBarista(coffeeTeam):
	"""Manager class with appropriate functions"""
	
	def get_drink_price(self, drink_id):
		"""return drink price"""
		
		pass
	def make_order(self, date, count, price, seller_id, drink_id):
		"""make order and save it into DB"""
		
		pass
	def get_members(self, role="barista"):
		"""get the list of all Barista"""
		
		connection = sqlite3.connect(self.db)
		with connection:
			result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
			data = result.fetchall()
			return data