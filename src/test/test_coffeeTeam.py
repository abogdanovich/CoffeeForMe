#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeTeam
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
import sys
import func
import pytest

test_db = "test_db.db"

"""
coffeeTeam test suit:
team_tc01: 		create a new barista
team_tc02: 		create a new manager
team_tc02_1:	create member with empty params 
team_tc03: 		get exists member details
team_tc04: 		get NON exists member details (negative)
team_tc05: 		drop all tables
"""

def test_team_tc01():
	# team_tc01: create a new barista
	# name=None, role=None, password=None
	# id = 1
	manager = coffeeManager()
	result = manager.add_member("Kate","manager", "pass123", test_db)
	assert result > 0
	
def test_team_tc02():
	# team_tc01: create a new barista
	# name=None, role=None, password=None
	# id = 2
	barista = coffeeBarista()
	result = barista.add_member("Alice","barista", "pass123", test_db)
	assert result > 0
	
def test_team_tc02_1():
	# team_tc01: create a new barista
	# name=None, role=None, password=None
	manager = coffeeManager()
	result = manager.add_member("","", "", test_db)
	assert result == False
	
def test_team_tc03():
	# get exists member details
	# manager Kate with id = 1
	member = coffeeTeam()
	result = member.get_member("Kate","pass123", test_db)
	assert result[0] == 1
	
def test_team_tc04():
	# get NON exists member details (negative)
	member = coffeeTeam()
	result = member.get_member("Test","123", test_db)
	assert result == False	
	
def test_team_tc05():
	# drop table if exists
	member = coffeeTeam()
	result = member.drop_all_tables(test_db)
	assert result == True


	
