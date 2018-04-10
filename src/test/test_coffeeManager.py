#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeManager
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
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

def test_drop_init():
	# drop table if exists
	member = coffeeTeam()
	result = member.drop_all_tables(test_db)
	assert result == True
	
def init():
	# init accounts
	manager = coffeeManager()
	result1 = manager.add_member("Kate","manager", "pass123", test_db)
	barista = coffeeBarista()
	result2 = barista.add_member("Alice","barista", "pass123", test_db)
	
def test_manager_tc01():
	# add a new drink with correct params
	init()
	result = func.add_new_drink("Latte", 9.99, test_db)
	assert result > 0

def test_manager_tc02():
	# add a new drink (negative)
	result = func.add_new_drink("Latte", "no-price", test_db)
	assert result == False

def test_manager_tc03():
	# make order as non barista(negative)
	barista = coffeeBarista()
	result = barista.make_order("invalid_role", "12:12:12 - 04/11/2018", 1.99, 1, 1, test_db)
	assert result == False
	
def test_manager_tc04():
	# make order and save
	barista = coffeeBarista()
	barista.make_order("barista", "12:12:12 - 04/11/2018", .99, 2, 1, test_db)
	barista.make_order("barista", "12:12:12 - 04/11/2018", 1.99, 2, 1, test_db)
	barista.make_order("barista", "12:12:12 - 04/11/2018", 5.99, 2, 1, test_db)
	barista.make_order("barista", "12:12:12 - 04/11/2018", 10.99, 2, 1, test_db)
	manager = coffeeManager()
	result = manager.get_revenue(test_db)
	assert result[1] == 19.96