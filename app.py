from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__) 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='srf*123'
app.config['MYSQL_DB']='flaskapp'
mysql=MySQL(app)
  
@app.route("/")
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM login")
    fetchdata=cur.fetchall()
    cur.close()
    return render_template("login.html",data=fetchdata)

if __name__=="__main__":
    app.run(debug=True)
