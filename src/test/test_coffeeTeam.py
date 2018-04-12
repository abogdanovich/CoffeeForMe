#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeTeam
"""

from coffee import coffeeTeam
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

def test_team_tc01():
	# team_tc01: create a new barista
	user = coffeeTeam(**manager)
	assert user.name == "Alex"
	
def test_team_tc02():
	# team_tc01: create a new barista
	user = coffeeTeam(**barista)
	assert user.name == "Max"
	
def test_team_tc02_1():
	# team_tc01: create a new barista
	manager = {"name": "Alex", "db": "test_db"}
	user = coffeeTeam(**manager)
	assert user.name == "Alex"
	
def test_team_tc03():
	# get exists member details
	user = coffeeTeam(**barista)
	assert user.uid == 2



	
