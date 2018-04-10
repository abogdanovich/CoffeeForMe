#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeBarista
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
import sys
import func
import pytest

test_db = "test_db.db"

"""
coffeeBarista test suit:
barista_tc01: make order and save
"""

def test_drop_init():
	# drop table if exists
	member = coffeeTeam()
	result = member.drop_all_tables(test_db)
	assert result == True
	
def test_init():
	# init accounts
	manager = coffeeManager()
	result1 = manager.add_member("Kate","manager", "pass123", test_db)
	barista = coffeeBarista()
	result2 = barista.add_member("Alice","barista", "pass123", test_db)
	
def test_barista_tc01():
	# make order and save
	barista = coffeeBarista()
	result = barista.make_order("barista", "12:12:12 - 04/11/2018", 1.99, 2, 1, test_db)
	assert result > 0	
