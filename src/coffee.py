#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Project classes are placed here.
"""
import sqlite3
import os

# set the current script dir 
current_dir = os.path.dirname(os.path.realpath(__file__))


class coffeeTeam(object):
	"""Base class"""
	
	def drop_all_tables(self, db="{}/db.db".format(current_dir)):
		"""remove all db tables"""
		data = False
		try:
			connection = sqlite3.connect(db)
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
					
	def get_member(self, name=None, password=None, db="{}/db.db".format(current_dir)):
		"""get the list of all team members"""
		data = False
		try:
			connection = sqlite3.connect(db)
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

	def add_member(self, name=None, role=None, password=None, db="{}/db.db".format(current_dir)):
		"""add new member"""
		data = False
		if (name != "") and (password != ""):
			
			try:
				connection = sqlite3.connect(db)
				with connection:
					connection.execute('''CREATE TABLE IF NOT EXISTS team (
									   id INTEGER PRIMARY KEY AUTOINCREMENT,
									   name TEXT NOT NULL,
									   password TEXT NOT NULL,
									   role TEXT NOT NULL
									   );''')
					if (role is None):
						role = 'unknown'
					connection.execute("INSERT INTO team (name, password, role) VALUES (?,?,?);", (name, password, role))
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
	
	def get_revenue(self, db="{}/db.db".format(current_dir)):
		"""generate Manager revenue report in summary table"""
		data = False
		total = 0
		try:
			connection = sqlite3.connect(db)
			with connection:
				result = connection.execute("""
					SELECT team.id, team.name as barman, COUNT(*) as sales, SUM(orders.price) as total
					FROM 'orders', 'team' 
					WHERE orders.seller_id=team.id
					GROUP BY team.id
					ORDER BY total DESC
				""")
				data = result.fetchall()
				for item in data:
					total += item[3]
				# return: barman | sales | sum 
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data, total					
		
	def get_member(self, role="manager", db="{}/db.db".format(current_dir)):
		"""get the list of all Managers"""
		data = False
		try:
			connection = sqlite3.connect(db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
				data = result.fetchall()
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data
	
	def add_drink(self, name, price, db="{}/db.db".format(current_dir)):
		"""add a new drink into db"""
		data = False
		try:
			connection = sqlite3.connect(db)
			with connection:
				connection.execute('''CREATE TABLE IF NOT EXISTS drink (
								   id INTEGER PRIMARY KEY AUTOINCREMENT,
								   name TEXT NOT NULL,
								   price REAL NOT NULL
								   );''')
				connection.execute("INSERT INTO drink (name, price) VALUES (?,?);", (name, price))
				result = connection.execute("SELECT last_insert_rowid()")
				record_id = result.fetchone()
				# return a new record's ID
				data = record_id[0]
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		return data					


class coffeeBarista(coffeeTeam):
	"""Manager class with appropriate functions"""
	
	def get_drink_list(self, drink_id=None, db="{}/db.db".format(current_dir)):
		"""return drink price"""
		data = False
		connection = sqlite3.connect(db)
		with connection:
			if drink_id != None:
				result = connection.execute("SELECT * FROM drink WHERE id=?",(drink_id))
			else:
				result = connection.execute("SELECT * FROM drink")
			data = result.fetchall()
			return data		
		
	def make_order(self, role, date, price, seller_id, drink_id, db="{}/db.db".format(current_dir)):
		"""make order and save it into DB"""
		data = False
		if role == "barista":
			try:
				connection = sqlite3.connect(db)
				with connection:
					connection.execute('''CREATE TABLE IF NOT EXISTS orders (
									   id INTEGER PRIMARY KEY AUTOINCREMENT,
									   order_date DATETIME NOT NULL,
									   price REAL NOT NULL,
									   seller_id INTEGER NOT NULL,
									   drink_id INTEGER NOT NULL
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
	
	def get_member(self, role="barista", db="{}/db.db".format(current_dir)):
		"""get the list of all Barista"""
		data = False
		try:
			connection = sqlite3.connect(db)
			with connection:
				result = connection.execute("SELECT * FROM team WHERE role=?",(role,))
				data = result.fetchall()
		except sqlite3.Error as e:
			print "DB error: [{}]".format(e)
		finally:
			if connection:
				connection.close()
		return data				