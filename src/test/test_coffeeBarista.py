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
barista_tc02: make order and do not save
barista_tc03: get revenue report for manager (negative)
barista_tc04: get member
barista_tc05: get member (negative)
barista_tc06: get drink list
barista_tc07: get selected drink 
"""

