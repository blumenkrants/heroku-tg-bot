import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создание таблицы
#  cursor.execute("""CREATE TABLE table_clients
#                   (client_id text, 
#                    tg_id text, 
#                    name text, 
#                    email text, 
#                    phone text, 
#                    datetime_registration text, 
#                    is_active integer)""",
#                """CREATE TABLE table_client_actions
#                   (client_id text,
#                   date_time text,
#                   customer_id text,
#                   service_id text,
#                   cal_url text)""",              
#                 """CREATE TABLE table_customers
#                   (customer_id text,
#                   customer_name text,
#                   customer_jur_name text,
#                   customer_addr text,
#                   datetime_reg text,
#                   is_active integer)""",
#                   """CREATE TABLE table_cal_config
#                   (cal_id text,
#                   customer_id text,
#                   cal_url text,
#                   cal_user text,
#                   cal_password text,
#                   cal_type_id text)""",
#                   """CREATE TABLE table_cal_types
#                   (cal_type_id text,
#                   cal_type_name text)""",
#                   """CREATE TABLE table_services
#                   (service_id text,
#                   customer_id text,
#                   service_name text,
#                   price integer,
#                   created_datetime text)""",
#                   """CREATE TABLE table_barbers
#                   (barber_id text,
#                   barber_name text)""",
#                   """CREATE TABLE table_barbers2customers
#                   (b2c_id text,
#                   barber_id text,
#                   customer_id text)""",
#                   """CREATE TABLE table_barbers2services
#                   (b2s_id text,
#                   barber_id text,
#                   service_id text)""")


# Вставляем множество данных в таблицу используя безопасный метод "?"
# clients = [('id_228', 'calendar'),
#           ('id_455', 'caldav')]

# cursor.executemany("INSERT INTO table_cal_types VALUES (?,?)", clients)
# conn.commit()

# удаление таблицы 
# sql = "SELECT * FROM table_cal_types"
# cursor.execute(sql)
# print(cursor.fetchall())

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
sql = "SELECT * FROM table_cal_types"
master1 = "SELECT * FROM table_barbers"
cursor.execute(master1)
data_base = cursor.fetchall()
for masters in data_base:
    print(masters[1])



