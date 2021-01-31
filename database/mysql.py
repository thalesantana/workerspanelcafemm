import mysql.connector
from dotenv import load_dotenv
import os
import time
import datetime
import sys


class MysqlConnection:

    def __init__(self):
        load_dotenv()
        self.__host = os.getenv("DB_HOST")
        self.__user = os.getenv("DB_USER")
        self.__password = os.getenv("DB_PASSWORD")
        self.conn = ''
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database="painelworkers")
            print("Database Connected successfully!")
        except:
            print("Database Connection error!")
            sys.exit(0)

    def run_select(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            lista = cur.fetchall()
            return lista
        except Exception as e:
            return 'Error on run this SELECT: '+str(e)

    def run_insert_update(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            self.conn.commit()
            return 'row saved successfully.'
        except Exception as e:
            return 'Error on apply update or insert: '+str(e)

    def query_to_dict(self, query, args=(), one=False):
        cur = self.conn.cursor()
        cur.execute(query, args)
        r = [dict((cur.description[i][0], value)
                  for i, value in enumerate(row)) for row in cur.fetchall()]
        # cur.connection.close()
        return (r[0] if r else None) if one else r

    def disconnect(self):
        self.conn.close()


pass
