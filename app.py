from flask import Flask, render_template, request,redirect
from flaskext.mysql import MySQL
from datetime import datetime 
app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)

@app.route("/")
def index():
    sql = "SELECT * FROM `sistema`.`empleados`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    # print(empleados)
    conn.commit()
    return render_template("index.html",empleados=empleados)

@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/store",methods=["POST"])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    now= datetime.now()
    tiempo= now.strftime("%Y%H%M%S")
    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)

    sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
    datos=(_nombre,_correo,nuevoNombreFoto)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template("index.html")
    

@app.route("/destroy/<int:id>")
def destroy(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    sql="DELETE FROM `sistema`.`empleados` WHERE id=%s"
    cursor.execute(sql,id)
    conn.commit()
    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
    sql = "SELECT * FROM `sistema`.`empleados` WHERE id=%s;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,id)
    empleados=cursor.fetchall()
    conn.commit()
    
    # print(empleados)
    return render_template("edit.html",empleados=empleados)





@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    # _foto=request.files['txtFoto']
    id=request.form['txtID']

    datos=(_nombre,_correo,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "UPDATE `sistema`.`empleados` SET `nombre`=%s, `correo`=%s WHERE id=%s;"
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)