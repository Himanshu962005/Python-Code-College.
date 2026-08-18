# Q30.Study and Implementation of Database, Structured Query Language and Database Connectivity.
import mysql.connector;
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valtryek962005",
    database="TestDB"
)
print("Database Connected Successfully.")
con.close()