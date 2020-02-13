from datetime import datetime
import os
import sqlite3
import uuid

# set some stuff up
url = 'http://aimbot.energy'
now = str(datetime.now())
file = str(uuid.uuid4()) + '.html'
cmd = 'monolith ' + url + ' -o ' + file

# run monolith
stream = os.popen('monolith ' + url + ' -o ' + file)
output = stream.read()

# insert shit into db
conn = sqlite3.connect('web_scraper_thingy.sqlite3')
c = conn.cursor()

data = (now, url, file)

c.execute('INSERT into jobs (`datetime`,`url`,`file`) VALUES (?,?,?)', data)

conn.commit()
conn.close()