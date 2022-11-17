import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host = "localhost",
    user = "Bill",
    password = "mypassword",  
    database = "contacts" ,

)
mycursor = db.cursor(buffered=True)

