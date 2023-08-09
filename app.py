from flask import Flask,request,render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@0623",
)

cursor = conn.cursor()

database_name = "project1"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

cursor.execute(f"USE {database_name}")

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL
                )''')
conn.commit()


@app.route("/",methods=["GET","POST"])
def login():
    stud_data = []                         
    if request.method == "POST":  
        name = request.form['name']             
        email = request.form['email']   
        address = request.form['address']                 
        
        cursor.execute('INSERT INTO students (name, email, address) VALUES (%s, %s, %s)', (name, email, address))
        conn.commit()

        cursor.execute('SELECT * FROM students')
        stud_data = cursor.fetchall()

        return render_template("login.html", stud_data=stud_data)

    return render_template("login.html")
        
    
if __name__ == '__main__':
    app.run(debug=True)
    cursor.close()
    conn.close()