#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: main.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
import sys

if __name__ == '__main__':
	if (len(sys.argv) <= 1) or (sys.argv[1] == "-h"):
		print """
		____________________________________________________
		CofeeForMe v1.0 written by Alex Bogdanovich

		Script Usage: cofee.py [option] [-L output log gile]
		Options and arguments without login options:

		-i		: interactive mode
		
		-a 		: create a new coffee team member (coffee.py -a manager Alex passwd)
		-u		: login under specific user (coffee.py -u Alex passwd)
		____________________________________________________
		Options and arguments under logged user:
		-r		: view revenue report
		-c		: save barista's order 
		____________________________________________________
		"""
	else:
		if (sys.argv[1] == "-a"):
			"""add a new team member"""
			if (sys.argv[2] == "manager"):
				# coffe.py -a manager Alex pass123
				manager = coffeeManager(sys.argv[3],sys.argv[2], sys.argv[4])
			elif (sys.argv[2] == "barista"):
				# coffe.py -a barista Alex pass123
				barista = coffeeBarista(sys.argv[3],sys.argv[2], sys.argv[4])
			else:
				print "wrong team member role"
		elif (sys.argv[1] == "-d"):
			"""add a new drink into db"""
			pass
			
		if (sys.argv[1] == "-i"):
			"""interactive mode"""
			while True:
				print """
				1 - Add a new CoffeForMe team member
				2 - Login
				0 - Exit
				"""
				selection = raw_input("Choose the menu item below: ")
				if (not selection) or (selection == "q"): break
				elif (selection == "1"):
					"""add a new coffee team member"""
					new_member = []
					user_input = raw_input("Let's add a new CoffeeForMe team member: [manager|barista]? ")
					if (user_input == "manager"):
						# ask all what we need
						new_member.append(user_input)
						user_input = raw_input("Please enter user name and password ")
						user_input = user_input.split()
						new_member.append(user_input[0])
						new_member.append(user_input[1])
						# create a new team member
						barista = coffeeTeam(new_member[1],new_member[0],new_member[2])
					elif (user_input == "barista"):
						# ask all what we need
						new_member.append(user_input)
						user_input = raw_input("Please enter user name and password ")
						user_input = user_input.split()
						new_member.append(user_input[0])
						new_member.append(user_input[1])
						# create a new team member
						manager = coffeeTeam(new_member[1],new_member[0],new_member[2])
				elif (selection == "2"):
					# try to login
					user_input = raw_input("Please enter user name and password ")
					user_input = user_input.split()
					member = coffeeTeam()
					res = member.get_member(user_input[0], user_input[1])
					print res #returned 4 ????
				elif (selection == "0"):
					break

				
	
	
