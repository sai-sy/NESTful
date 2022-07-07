import mysql.connector
from datetime import datetime
import datetime

db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
)

mycursor = db.cursor()
mycursor.execute('SHOW DATABASES')
print(mycursor.fetch)