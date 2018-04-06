#!/usr/bin/env python
# -*- coding: utf-8 -*-
from coffee import coffeeBar, coffeeManager, coffeeBarista

""" File name: main.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Date created:	4/19/2018
	Python Version: 2.7
	
"""



if __name__ == '__main__':
	coffee_manager = coffeeManager("Alex", "manager")
	coffee_manager = coffeeManager("Max", "brista")
	print (coffee_manager.get_member())