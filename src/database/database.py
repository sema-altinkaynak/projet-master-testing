import sqlite3
import os
from sqlite3 import Error


class Database:

    def __init__(self):
        self.connexion = None

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            self.connexion = sqlite3.connect(
                r""+os.getcwd() + "/calculatrice.db")
            #print(sqlite3.version)
        except Error as e:
            print(e)
            ##self.create_table()
        return self.connexion



    def close_connexion(self):
        self.connexion.close()
