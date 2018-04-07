#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: main.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
import sys




if __name__ == '__main__':
	#for param in sys.argv:
	#	print param
	
	if len(sys.argv) <= 1:
		print "Please type `cofee.py -h` for more details"
		
	else:
		
		if (param[2] == "-h"):
			print """
			CofeeForMe v1.0 written by Alex Bogdanovich
			Make your life better :)
			---
			Script Usage: cofee.py [option] [-L output log gile]
			Options and arguments:
			-h	: help script
			-m	: create a new coffee manager
			-b	: create a new coffee barman
			-d	: creare a new drink with options
			"""
	#team = coffeeTeam()
	#manager = coffeeManager()
	#barista = coffeeBarista()
	
	
