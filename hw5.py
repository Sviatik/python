import os
import sqlite3
from sys import argv

db = argv[1]

sql = '''UPDATE ServerPorts
         SET port_number=443
         WHERE id IN 
         (SELECT ServerPorts.id FROM ServerPorts
         INNER JOIN Servers
         ON Servers.servertypes_id=ServerTypes.id
         INNER JOIN ServerTypes
         ON ServerProjects.servers_id=Servers.id
         INNER JOIN ServerProjects
         ON ServerPorts.servers_id=Servers.id
         INNER JOIN Projects
         ON ServerProjects.projects_id=Projects.id
         WHERE ServerTypes.type_name='apache' and Projects.proj_name='Project3');'''

conn = sqlite3.connect(db)
cur = conn.cursor()
exe = cur.execute(sql).fetchall()
conn.commit()

conn.close()