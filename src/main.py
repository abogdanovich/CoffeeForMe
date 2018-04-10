#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File name: main.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
"""

from coffee import coffeeTeam, coffeeManager, coffeeBarista
import sys
import func

# session variables
session_user = None
session_role = None
session_id = None

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
				`app -u user passwd add_drink "drink_name" "drink_price"`
				`app -u user passwd order_drink "drink_name" "drink_options"`
		____________________________________________________
		"""
	else:
		if (sys.argv[1] == "-a"):
			# add a new team member
			if (sys.argv[2] == "manager"):
				manager = coffeeManager()
				manager.add_member(sys.argv[3],sys.argv[2], sys.argv[4])
			elif (sys.argv[2] == "barista"):
				barista = coffeeBarista()
				barista.add_member(sys.argv[3],sys.argv[2], sys.argv[4])
			else:
				func.log("error", "Wrong member's role is selected: manager|barista")
		if (sys.argv[1] == "-u"):
			# run command under user login + passwd {command}
			if (len(sys.argv) < 4):
				print """
				Options and arguments under logged user:
				`app -u user passwd get_report`
				`app -u user passwd get_drinks`
				`app -u user passwd add_drink "drink_name" "drink_price"`
				`app -u user passwd order_drink "drink_name" "drink_options"`
				"""
			else:
				user = func.try_to_login(sys.argv[2],sys.argv[3])
				if not user: 
					func.log("error", "Wrong user or password is used")
				else:
					if (sys.argv[4] == "get_report"):
						if user[2] == "manager":
							func.get_revenue_report()
					elif (sys.argv[4] == "get_drinks"):
						func.get_drinks()
						print "Drink options"
						func.get_options()
							
					elif (sys.argv[4] == "add_drink"):
						if user[2] == "manager":
							# regular add drink into db under manager
							func.add_new_drink(sys.argv[5], sys.argv[6])
					elif (sys.argv[4] == "order_drink"):
						# make an order under barista
						if user[2] == "barista":
							func.save_order(session_role, user[0], sys.argv[5], list(sys.argv[5]), user[0])
		if (sys.argv[1] == "-i"):
			# interactive mode
			while True:
				if (session_user):
					# check user session permissions
					if (session_role == "manager"):
						func.show_manager_menu(session_user, session_role)
					else:
						func.show_barista_menu(session_user, session_role)
				else:
					func.show_regular_menu()
				selection = raw_input("Select menu option: ")
				if (not selection) or (selection == "q"): break
				elif (selection == "1"):
					# add a new coffee team member
					func.add_new_team_member()
				elif (selection == "2"):
					if (session_user):
						session_user = None
						session_role = None
						session_id = None
						func.log("warning", "User is logged out")
					else:
						try_to_login = func.try_to_login()
						if (try_to_login):
							session_id = try_to_login[0]
							session_user = try_to_login[1]
							session_role = try_to_login[2]
				elif (selection == "0"):
					break
				elif (selection == "3"):
					# create a new revenue report
					if (session_role != "manager"):
						print "You can't run this option"
						continue
					else:
						# make the final report
						func.get_revenue_report()
				elif (selection == "4"):
					# check a drink price and save an order
					if (session_role != "barista"):
						print "You can't run this option"
						continue
					else:
						# make the order and save it
						func.save_order(session_role, session_id)

				elif (selection == "9"):
					# add a new drink into db
					if (session_role != "manager"):
						print "You can't run this option"
						continue
					else:
						func.add_new_drink()