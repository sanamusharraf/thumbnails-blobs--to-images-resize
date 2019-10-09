import mysql.connector
import os
from PIL import Image

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
my_database=mydb.cursor()
sql_statement = "SELECT programID,thumbimage FROM `log_programbm` group by programID order by insertDate"
my_database.execute(sql_statement)
output = my_database.fetchall()

Thisfolder = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(Thisfolder , "pictures")
for x in output:
  name = str(x[0])
  picture = os.path.join(folder, "{names}.png".format(names=name))
  
  with open(picture,'wb') as file:
    file.write(x[1])
    file.close()

  img = Image.open(picture)  
  img = img.resize((50, 50)) 
  img.save(picture) 
