#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Project classes are placed here.
	Updated version v2 with flexibility and correct OOP
	
"""
import sqlite3
import os

# set the current script dir 
current_dir = os.path.dirname(os.path.realpath(__file__))

class coffeeTeam(object):
	"""Base class"""
	def __init__(self, **kwargs):
		"""constructor of a base class"""
		if kwargs is not None and len(kwargs) >= 2:
			try:				
				if "db" in kwargs:
					self.db = kwargs["db"]	
				else:
					self.db = "{}/db.db".format(current_dir)
				self.name = kwargs["name"]
				self.passwd = kwargs["passwd"]
				if "role" in kwargs:
					self.role = kwargs["role"]
				else:
					# by default
					self.role = "barista" 
				self.logged = False
				# try to login or we'll save it as a new member
				self.make_login()
				if not self.logged:
					self.save_member()
					print("A new member is saved into self.db {}".format(self.uid))
			except Exception as e:
				print e
		else:
			print "not enough params"

	def make_login(self):
		"""try to login"""
		# new member
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE name=? AND password=?", (self.name, self.passwd))
				user = result.fetchone()
				if (user):
					self.uid = user[0]
					self.name = user[1]
					self.role = user[3]
					self.logged = True
		except sqlite3.Error as e:
			print "DB error make_login: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		
	def save_member(self):
		"""save team member into self.db"""
		#if self.name is not None and self.passwd is not None and self.role is not None:
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				connection.execute('''CREATE TABLE IF NOT EXISTS team (
								   id INTEGER PRIMARY KEY AUTOINCREMENT,
								   name TEXT NOT NULL,
								   password TEXT NOT NULL,
								   role TEXT NOT NULL
								   );''')
				connection.execute("INSERT INTO team (name, password, role) VALUES (?,?,?);", (self.name, self.passwd, self.role))
				result = connection.execute("SELECT last_insert_rowid()")
				record_id = result.fetchone()
				# return a new record's ID
				self.uid = record_id[0]
				self.logged = True 
		except sqlite3.Error as e:
			print "DB error save_member: [{}]".format(e)

	@property
	def member(self):
		"""get member details"""
		if self.logged:
			return self.uid, self.name, self.role
	
	def get_revenue_data(self):
		"""get the revenue table"""
		data = False
		if self.logged and self.role == "manager":
			try:
				connection = sqlite3.connect(self.db)
				with connection:
					result = connection.execute("""
						SELECT team.id, team.name as barman, COUNT(*) as sales, SUM(orders.price) as total
						FROM 'orders', 'team' 
						WHERE orders.seller_id=team.id
						GROUP BY team.id
						ORDER BY total DESC
					""")
					data = result.fetchall()
					
			except sqlite3.Error as e:
				print "DB error: [{}]".format(e)
			finally:
				if connection:
					connection.close()
		else:
			print "permission error"
		return data
	
	def save_drink(self, **kwargs):
		"""add a new drink"""
		data = False
		if self.logged and self.role == "manager":
				if kwargs is not None and len(kwargs) >= 2:
					try:
						connection = sqlite3.connect(self.db)
						with connection:
							connection.execute('''CREATE TABLE IF NOT EXISTS drink (
											   id INTEGER PRIMARY KEY AUTOINCREMENT,
											   name TEXT NOT NULL,
											   price REAL NOT NULL
											   );''')
							connection.execute("INSERT INTO drink (name, price) VALUES (?,?);", (kwargs["name"], kwargs["price"]))
							result = connection.execute("SELECT last_insert_rowid()")
							record_id = result.fetchone()
							# return a new record's ID
							data = record_id[0]
					except sqlite3.Error as e:
						print "DB error: [{}]".format(e)
		else:
			print "permission error"
		return data
	
	def get_drink_list(self):
		"""return drink price"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("SELECT * FROM drink")
				data = result.fetchall()
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		return data

	def save_order(self, **kwargs):
		"""make order and save it into DB"""
		data = False
		if self.logged and self.role == "barista":
			if kwargs is not None and len(kwargs) >= 3:
				try:
					connection = sqlite3.connect(self.db)
					with connection:
						connection.execute('''CREATE TABLE IF NOT EXISTS orders (
										   id INTEGER PRIMARY KEY AUTOINCREMENT,
										   order_date DATETIME NOT NULL,
										   price REAL NOT NULL,
										   seller_id INTEGER NOT NULL,
										   drink_id INTEGER NOT NULL
						);''')
						
						connection.execute('INSERT INTO orders (order_date, price, seller_id, drink_id) VALUES (?,?,?,?);', (kwargs["datetime"], kwargs["price"], self.uid, kwargs["drink_id"]))
						result = connection.execute("SELECT last_insert_rowid()")
						record_id = result.fetchone()
						# return a new record's ID
						data = record_id[0]
				except sqlite3.Error as e:
					print "DB error: [{}]".format(e)
				finally:
					if connection:
						connection.close()
		else:
			print "permission error"			
		return data
	
	def drop_test_tables(self):
		"""remove all db tables"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("DROP TABLE IF EXISTS 'team';")
				result = connection.execute("DROP TABLE IF EXISTS 'orders';")
				result = connection.execute("DROP TABLE IF EXISTS 'drinks';")
				data = True
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data