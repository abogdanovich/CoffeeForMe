#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File name: coffee.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	pytest for class: coffeeBarista
"""

from coffee import coffeeTeam
import sys
import func
import pytest

test_db = "test_db.db"

"""
coffeeBarista test suit:
barista_tc01: make order and save
"""

manager = {"name": "Alex", "role": "manager", "passwd": "123", "db": "test_db"}
barista = {"name": "Max", "role": "barista", "passwd": "123", "db": "test_db"}
drink1 = {"name": "latte", "price": 1.99, "db": "test_db"}
drink2 = {"name": "americano", "price": 2.99, "db": "test_db"}
order1 = {"barista": 1, "datetime": "10:41-04-12-18", "price": 4.99, "drink_id": 1, "db": "test_db"}
order2 = {"barista": 2, "datetime": "10:41-04-12-18", "price": 2.99, "drink_id": 2, "db": "test_db"}
	
# cleanup test db
user_m = coffeeTeam(**manager)
user_m.drop_test_tables()
user_m = coffeeTeam(**manager)
user_b = coffeeTeam(**barista)

def test_barista_tc01():
	# make order and save
	
	func.save_order(user_b, **order1)
	grand_total = func.get_revenue_report(user_m)
	assert grand_total == 4.99
