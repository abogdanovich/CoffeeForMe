#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


""" File name: coffee_db.py
    Author:	Alex Bogdaovich
	Email: bogdanovich.alex@gmail.com
	Date created:	4/19/2018
	Python Version: 2.7
	DB Class to work with data
	
"""

class DB(object):    
    """DB base class to work with SQLite3 databases"""

    def __init__(self, database='coffee.db', statements=None):
        """Initialize params"""
        
        self.database = database
        if statements is None:
            statements = ''
        self.connect()

    def connect(self):
        """Connect function to db"""
        
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True

    def close(self): 
        """Close db"""
        
        self.connection.commit()
        self.connection.close()
        self.connected = False

    def execute(self, statements):
        """Execute SQL query"""

        self.cursor.execute(statements)
        #self.cursor.commit()
        # get the selected data
        return self.cursor.fetchall()

if __name__ == '__main__':     
    statement = ('CREATE TABLE Member (id INTEGER, name TEXT);')                    
    #setup
    db = DB("coffee.db", statement)
    #a single statement
    db.execute(statement)
    db.execute("INSERT INTO Member (id, name) values (1, 'Alex')")
    
    #retrieving multiple query results
    query = "SELECT * FROM Member"
    for result in db.execute(query):
        print result
    db.close()