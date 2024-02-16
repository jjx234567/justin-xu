import urllib.request, urllib.parse, urllib.error #inputing project data into database
import http
import sqlite3
import json
import time
import ssl
import sys

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('/Users/Justin/Desktop/py4e/justin-xu/projects.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Projects (title TEXT, description TEXT, img TEXT)''')

fh = open("/Users/Justin/Desktop/py4e/justin-xu/projects.txt")
count = 0
nofound = 0
for line in fh:
    if count > 100 :
        print('Retrieved projects, restart to retrieve more')
        break

    projecttitle = line.strip().split(",")[0].split(": ")[1]
    projectimg = line.strip().split(",")[2].split(": ")[1]
    projectdesc = line.strip().split(",")[1].split(": ")[1]
    print(projecttitle, projectdesc, projectimg)
    cur.execute("SELECT * FROM Projects WHERE title= ?",
        (memoryview(projecttitle.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database, updating the row", projecttitle)
        cur.execute('''UPDATE Projects 
                SET title = ?, description = ?, img = ?
                WHERE title = ?''', 
                (memoryview(projecttitle.encode()), memoryview(projectdesc.encode()), memoryview(projectimg.encode()), memoryview(projecttitle.encode()) ) )
        conn.commit()
        continue
    except:
        pass
    count = count + 1

    cur.execute('''INSERT INTO Projects (title, description, img)
                VALUES ( ?, ?, ?)''', (memoryview(projecttitle.encode()), memoryview(projectdesc.encode()), memoryview(projectimg.encode()) ) )
    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run projectdump.py to read the data from the database so you can vizualize it on a map.")

