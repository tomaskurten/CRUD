from multiprocessing.forkserver import connect_to_new_process
from flask import Flask,render_template, request, redirect, send_from_directory
import os
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)

@app.route('/')
def index():
    sql="INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (Null, 'juan', 'juan@mail.com', 'foto1.png');"

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # return "<h1>Hola Codo a Codo!</h1> <p>Todo a salido bien.</p><p>Chau</p>"
    return render_template('index.html')


@app.route('/create')
def create():
 return render_template('create.html')


# @app.route('/store', methods=['POST'])
# def storage():
#     sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', '');"
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     return render_template('index.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']

    datos=(_nombre, _correo,_foto.filename)

    sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
    # sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', '');"

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

if __name__=='__main__':
 app.run(debug=True)