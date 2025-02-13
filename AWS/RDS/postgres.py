import psycopg2

db_host = "database-2.czsimoaie7x7.ap-south-1.rds.amazonaws.com"
db_name = 'test_name'
db_user = 'postgres'
db_pass = 'progknowledge'

connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
print("Connected to the database")

cursor = connection.cursor()
cursor.execute('SELECT version()')
db_version = cursor.fetchone()
print(db_version)

cursor.close()