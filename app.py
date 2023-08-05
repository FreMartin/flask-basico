from flask import Flask, render_template;
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ElMartin'
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', users=data)