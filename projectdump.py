import sqlite3 # Loads data from splite into javascript file(projects.js)
import json
import codecs

conn = sqlite3.connect('/Users/Justin/Desktop/py4e/justin-xu/projects.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Projects')
fhand = codecs.open('/Users/Justin/Desktop/py4e/justin-xu/projects.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    title = str(row[0].decode())
    description = str(row[1].decode())
    image = str(row[2].decode())

    try :
        print(title, description, image)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "['"+str(title)+"','"+str(description)+"', '"+image+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

