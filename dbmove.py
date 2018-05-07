import sqlite3
import os

conn = sqlite3.connect('benri.db')
curs = conn.cursor()

r = open('script.txt', encoding="utf8", errors='ignore' 'r')
R = r.readlines()

i = 0
for row in range(len(R)):
       if i+2 <= len(R):
              curs.execute('INSERT INTO tasks(eng,jap) VALUES (?,?)',[R[i],R[i+1]])
              i = i+2
        
conn.commit()   
