import psycopg2

conn = psycopg2.connect(dbname='mydatabase', user='postgres', 
                        password='qwerty', host='192.168.0.100')
cursor = conn.cursor()
cursor.execute("INSERT INTO info (name, service, date, time, number) VALUES ('1', 'Cheese', '1', '2','2')")
conn.commit()
conn.close()

