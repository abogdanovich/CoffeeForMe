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
	
	def __init__(self, name=None, role=None, password=None, db="db.db"):
		"""save team member with his name and company role into db"""
		self.name = name
		self.role = role
		self.password = password
		self.db = db
		if (name is not None):
			self.add_member()
		
	def get_member(self, name=None, password=None):
		"""get the list of all team members"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE name=? AND password=?", (name, password))
				check_user = result.fetchone()
				if (check_user):
					data = (check_user[0], check_user[1], check_user[3])
				else: return False
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data

	def add_member(self):
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				connection.execute('''CREATE TABLE IF NOT EXISTS team (
								   id INTEGER PRIMARY KEY AUTOINCREMENT,
								   name TEXT,
								   password TEXT,
								   role TEXT
								   );''')
				if (self.role is None):
					self.role = 'unknown'
				connection.execute("INSERT INTO team (name, password, role) VALUES (?,?,?);", (self.name, self.password, self.role))
				result = connection.execute("SELECT last_insert_rowid()")
				record_id = result.fetchone()
				# return a new record's ID
				data = record_id[0]
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data					


class coffeeManager(coffeeTeam):
	"""Manager class with appropriate functions"""
	
	# TODO - FAILED when no records in orders!!!! fix that
	def get_revenue_report(self):
		"""generate Manager revenue report in summary table"""
		data = False
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
				# return: barman | sales | sum 
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data						
		
	def get_member(self, role="manager"):
		"""get the list of all Managers"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
				data = result.fetchall()
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data
	
	def add_drink(self, name, price):
		"""add a new drink into db"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				connection.execute('''CREATE TABLE IF NOT EXISTS drink (
								   id INTEGER PRIMARY KEY AUTOINCREMENT,
								   name TEXT,
								   price REAL
								   );''')
				connection.execute("INSERT INTO drink (name, price) VALUES (?,?);", (name, price))
				result = connection.execute("SELECT last_insert_rowid()")
				record_id = result.fetchone()
				# return a new record's ID
				data = record_id[0]
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data					


class coffeeBarista(coffeeTeam):
	"""Manager class with appropriate functions"""
	
	def get_drink_list(self, drink_id=None):
		"""return drink price"""
		connection = sqlite3.connect(self.db)
		with connection:
			if drink_id != None:
				result = connection.execute("SELECT * FROM drink WHERE id=?",(drink_id))
			else:
				result = connection.execute("SELECT * FROM drink")
			data = result.fetchall()
			return data		
		
	def make_order(self, date, price, seller_id, drink_id):
		"""make order and save it into DB"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				connection.execute('''CREATE TABLE IF NOT EXISTS orders (
								   id INTEGER PRIMARY KEY AUTOINCREMENT,
								   order_date DATETIME,
								   price REAL,
								   seller_id INTEGER,
								   drink_id INTEGER
				);''')
				
				connection.execute('INSERT INTO orders (order_date, price, seller_id, drink_id) VALUES (?,?,?,?);', (date, price, seller_id, drink_id))
				result = connection.execute("SELECT last_insert_rowid()")
				record_id = result.fetchone()
				# return a new record's ID
				data = record_id[0]
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data				
	def get_member(self, role="barista"):
		"""get the list of all Barista"""
		data = False
		try:
			connection = sqlite3.connect(self.db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
				data = result.fetchall()
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data				