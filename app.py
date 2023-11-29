from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/store",methods=["POST"])
def storage():
    nombre=request.form["txtNombre"]
    correo=request.form["txtCorreo"]
    datos=(nombre,correo)
    # foto=request.files["txtFoto"]
    sql="INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, 'foto4.jpg');"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template("index.html")
    

if __name__=="__main__":
    app.run(debug=True)