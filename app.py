from flask import Flask, render_template, request
# import pymysql
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'ap-south.connect.psdb.cloud'
app.config['MYSQL_USER'] = 'o1u9brd68nj795lm4a42'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_PAVYQAd5I6zfKZtRJmto3PdVgximyKYGJzp4fzlahyW'
app.config['MYSQL_DB'] = 'rishabhcareers'

mysql = MySQL(app)

# def sql_connector():
#   conn = pymysql.connect(
#     user='o1u9brd68nj795lm4a42',
#     password='pscale_pw_PAVYQAd5I6zfKZtRJmto3PdVgximyKYGJzp4fzlahyW',
#     db='rishabhcareers',
#     host='ap-south.connect.psdb.cloud',
#     ssl_ca="/etc/ssl/cert.pem")
#   c = conn.cursor()
#   return conn, c


@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    title = request.form('title')
    location = request.form'location')
    salary = request.form('salary')
    currency = request.form('currency')
    responsibilities = request.form'responsibilities')
    requirements = request.form('requirements')

    cursor = mysql.connection.cursor()
    cursor.execute(
      ''' INSERT INTO jobs VALUES(%s,%s,%s,%s,%s,%s)''',
      (title, location, salary, currency, responsibilities, requirements))
    mysql.connection.commit()
    cursor.close()
    return f"Done!!"
    # conn, c = sql_connector()
    # c.execute("INSERT INTO jobs VALUES ('{}' {} {} {} {} {})".format(
    #   title, location, salary, currency, responsibilities, requirements))
    # conn.commit()
    # conn.close()
    # c.close()

  return render_template('index.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0")

# pymysql, mysql-connector, mysql-connector-python
