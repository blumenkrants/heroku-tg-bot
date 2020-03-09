import os
import psycopg2

# DATABASE_URL = os.environ['postgres://sepdreekypiqhd:ac8d1d611f3d504f7c312d5b62c0e8d0319925773b62f747da1a3320ee0b3ee4@ec2-54-246-89-234.eu-west-1.compute.amazonaws.com:5432/d1d4qe3vqt296e']
#
# conn = psycopg2.connect(DATABASE_URL,
#                         sslmode='require')

conn = psycopg2.connect(host='ec2-54-246-89-234.eu-west-1.compute.amazonaws.com',
                        database='d1d4qe3vqt296e',
                        user='sepdreekypiqhd',
                        password='ac8d1d611f3d504f7c312d5b62c0e8d0319925773b62f747da1a3320ee0b3ee4')


cursor = conn.cursor()

sql = "SELECT * FROM barbershop_room"
cursor.execute(sql)
data_base = cursor.fetchall()
print(data_base)


# SELECT * FROM INFORMATION_SCHEMA.TABLES
#
# \dt *.*
#
# как сменить используемую схему в постгре

