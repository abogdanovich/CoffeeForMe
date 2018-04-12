#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: main.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
"""

from coffee import coffeeTeam
import sys
import func

# session variables
session_user = None
session_role = None
session_id = None
user = None

if __name__ == '__main__':
	if (len(sys.argv) <= 1) or (sys.argv[1] == "-h"):
		print """
		____________________________________________________
		CofeeForMe v1.0 written by Alex Bogdanovich

		Script Usage: cofee.py [option] [-L output log gile]
		Options and arguments without login options:

		-i		: interactive mode
		-a 		: create a new coffee team member: `app -a manager|barista user passwd`
		____________________________________________________
		Options and arguments under logged user:
		-u		: run a command under user:
				`app -u user passwd get_report`
				`app -u user passwd get_drinks`
				`app -u user passwd add_drink "drink_name" {drink_price}`
				`app -u user passwd order_drink {drink_id} {drink_price}`
		____________________________________________________
		"""
	else:
		if (sys.argv[1] == "-a"):
			# add a new team member
			if (len(sys.argv) >= 5):
				params = {"name": sys.argv[3], "role": sys.argv[2], "passwd": sys.argv[4]}
				func.add_new_team_member(**params)
			else:
				func.log("error", "wrong number of params in new member")
				print("ERROR: wrong number of params")
		if (sys.argv[1] == "-u"):
			# run command under user login + passwd {command}
			if (len(sys.argv) < 4):
				print """
				Options and arguments under logged user:
				`app -u user passwd get_report`
				`app -u user passwd get_drinks`
				`app -u user passwd add_drink "drink_name" {drink_price}`
				`app -u user passwd order_drink {drink_id} {drink_price}`
				"""
			else:
				params = {"name": sys.argv[2], "passwd": sys.argv[3]}
				# check the user credentials
				user = func.make_login(**params)
				
				if user.role == "manager":
					# available only for manager
					if (sys.argv[4] == "get_report"):	
						func.get_revenue_report(user)
					elif (sys.argv[4] == "get_drinks"):
							func.show_drinks(user)
							print "Drink options"
							func.show_options()
					elif (sys.argv[4] == "add_drink"):
							params = {"name": sys.argv[5], "price": sys.argv[6]}
							func.add_new_drink(user, **params)
				if user.role == "barista":
					# available only for barista
					if (sys.argv[4] == "order_drink"):	
							# TODO repair
							# order_drink "drink_name" "drink_options"
							order = {"barista": user.uid, "drink_id": sys.argv[5], "price": sys.argv[6]}
							func.save_order(user, **order)
		if (sys.argv[1] == "-i"):
			# interactive mode
			while True:
				if user:
					if user.role == "manager": func.show_menu_manager(user)
					elif user.role == "barista": func.show_menu_barista(user)
				else:
					func.show_menu()
					
				selection = raw_input("Select menu option: ")
				if not selection or selection == "q": break
				elif selection == "1":
					# add a new coffee team member
					user = func.add_new_team_member()
				elif selection == "2":
					if user:
						user = None
						func.log("warning", "Close user session")
					else:
						# login as manager
						#params = {"role": "manager"}
						user = func.make_login()

				elif selection == "0": break
				elif selection == "3" and user.role == "manager":
						# make the final report
						func.get_revenue_report(user)
				elif selection == "4" and user.role == "barista":
						# make the order and save it
						func.save_order(user)

				elif (selection == "9") and user.role == "manager":
						func.add_new_drink(user)