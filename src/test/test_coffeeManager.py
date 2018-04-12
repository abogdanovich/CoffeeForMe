#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeManager
"""

from coffee import coffeeTeam
import sys
import func
import pytest

test_db = "test_db.db"

"""
coffeeManager test suit:
manager_tc01: add a new drink with correct params
manager_tc02: add a new drink (negative)
manager_tc03: make order as non barista(negative)
manager_tc04: check the GRAND TOTAL 
"""

manager = {"name": "Alex", "role": "manager", "passwd": "123", "db": "test_db.db"}
barista = {"name": "Max", "role": "barista", "passwd": "123", "db": "test_db.db"}
drink1 = {"name": "latte", "price": 1.99, "db": "test_db.db"}
drink2 = {"name": "americano", "price": 2.99, "db": "test_db.db"}
order1 = {"barista": 1, "datetime": "10:41-04-12-18", "price": 4.99, "drink_id": 1, "db": "test_db.db"}
order2 = {"barista": 2, "datetime": "10:41-04-12-18", "price": 2.99, "drink_id": 2, "db": "test_db.db"}	

# cleanup test db
user_m = coffeeTeam(**manager)
user_m.drop_test_tables()
user_m = coffeeTeam(**manager)
user_b = coffeeTeam(**barista)

def test_manager_tc01():
	# add a new drink with correct params
	
	result = func.add_new_drink(user_m, **drink1)
	assert result > 0

def test_manager_tc02():
	# add a new drink (negative)
	
	result = func.add_new_drink(user_b, **drink1)
	assert result == False

def test_manager_tc03():
	# make order as non barista(negative)
	result = func.save_order(user_m, **order1)
	assert result == False
	
def test_manager_tc04():
	# make order and save
	func.save_order(user_b, **order1)
	func.save_order(user_b, **order1)
	func.save_order(user_b, **order1)
	
	grand_total = func.get_revenue_report(user_m)
	assert grand_total == 14.97