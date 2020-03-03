import mysql.connector
import base64
import io
import PIL.Image
with open("/Users/dmitriy/Downloads/578d905c4f11215600fbe8a4.jpg", "rb") as f:
    photo = f.read()
encodestring = base64.b64encode(photo)

db = mysql.connector.connect(host='mysql.j949396.myjino.ru', 
                            database='j949396', 
                            user='j949396', 
                            password='qwerty')
mycursor=db.cursor()

sql = "INSERT INTO table_photo values(%s)"
mycursor.execute(sql,(encodestring,))
db.commit()

sql1 = "SELECT * from table_photo"
mycursor.execute(sql1)

data = mycursor.fetchall()
data1 = base64.b64decode(data[0][0])
file_like = io.BytesIO(data1)
img = PIL.Image.open(file_like)
img.show()
db.close()
