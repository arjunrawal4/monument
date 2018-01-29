import MySQLdb
from intercom.client import Client

intercom = Client(personal_access_token='my_personal_access_token') #logs into intecom

db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="monument") #connects to db
cur = db.cursor() 
cur.execute("SELECT * FROM users")
   
for user in cur.fetchall() :
    user = intercom.users.create(email=user[1], name=user[2]) #creates user with email and name