#import database
import sqlite3
con = sqlite3.connect("tutorial.db")

#create cursor
cur = con.cursor()

#create a table with three columns
cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute('SELECT name FROM sqlite_master')
res.fetchone()

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None


'''
I have no idea what I am doing here, and it isnt making any sense yet. 
I may re-attempt it with some youtube tutorials'''