# from flask import Flask, render_template, request
# import pymysql
# from flask_mysqldb import MySQL
import pyrebase

# app = Flask(__name__)


Config = {
  "apiKey": "AIzaSyBRSHFaFYUCikwyJth-r2FHUa2Cjsg4hbw",
  "authDomain": "python-firebase-eacea.firebaseapp.com",
  "projectId": "python-firebase-eacea",
  "databaseURL":"https://python-firebase-eacea-default-rtdb.firebaseio.com/",
  "storageBucket": "python-firebase-eacea.appspot.com",
  "messagingSenderId": "481606708631",
  "appId": "1:481606708631:web:d1fdfe2f4c409f050ea8d2"
};

firebase =pyrebase.initialize_app(Config)
database= firebase.database()

data={"Age":21,"Name":"Hello"}
database.push(data)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'rishabhcareers'

# mysql = MySQL(app)

# def sql_connector():
#   conn = pymysql.connect(
#     user='o1u9brd68nj795lm4a42',
#     password='pscale_pw_PAVYQAd5I6zfKZtRJmto3PdVgximyKYGJzp4fzlahyW',
#     db='rishabhcareers',
#     host='ap-south.connect.psdb.cloud',
#     ssl_ca="/etc/ssl/cert.pem")
#     c = conn.cursor()
#     return conn, c


# @app.route('/')
# def home():
  
  # cursor = mysql.connection.cursor()
  # if request.method == 'POST':
  # id = request.form('id')
  # title = request.form('title')
  # location = request.form('location')
  # salary = request.form('salary')
  # currency = request.form('currency')
  # responsibilities = request.form('responsibilities')
  # requirements = request.form('requirements')
  # first = "Ravi"
  # last = "Kiran"
  # cursor.execute("INSERT INTO user(Fname,lname) VALUES(%s,%s)", (first, last))
  # mysql.connection.commit()
  # cursor.close()
  # return "success"
  # conn, c = sql_connector()
  # c.execute("INSERT INTO jobs VALUES ('{}' {} {} {} {} {})".format(
  #   title, location, salary, currency, responsibilities, requirements))
  # conn.commit()
  # conn.close()
  # c.close()


# if __name__ == '__main__':
#   app.run(host="0.0.0.0")

# pymysql, mysql-connector, mysql-connector-python
