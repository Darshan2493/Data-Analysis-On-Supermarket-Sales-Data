from flask import *
import pymysql as pm
db=pm.connect(host="localhost",user="root",password="",database="hostel")
cursor=db.cursor()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/allusers")
def allusers():
    q="SELECT * FROM boys"
    cursor.execute(q)
    result=cursor.fetchall()
    return render_template("allusers.html",data=result)
@app.route("/adduser",methods=['POST'])
def adduser():
    name=request.form['uname']
    contact=request.form['gcontact']
    room_no=request.form['groom']
    age=request.form['gage']
    insq="INSERT INTO boys(name,contact,room_no,age) VALUES ('{}','{}','{}','{}')".format(name,contact,room_no,age)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('allusers'))
    except:
        db.rollback()
        return "Error in Query"
@app.route("/delete")
def delete():
   id=request.args['id']
   delq="DELETE FROM boys WHERE id={}".format (id)
   try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for('allusers'))
   except:
        db.rollback()
        return "Error in Query"
@app.route("/edit")
def edit():
    id=request.args['id']
    se="SELECT * FROM boys WHERE id={}".format(id)
    cursor.execute(se)
    result=cursor.fetchone()
    return render_template('edit.html',data=result)
@app.route("/update", methods=['POST'])
def update():
     name=request.form['uname']
     contact=request.form['gcontact']
     room_no=request.form['groom']
     age=request.form['gage']
     id=request.form['uid']
     udq="UPDATE boys SET name='{}',contact='{}',room_no='{}',age='{}' WHERE id={}".format(name,contact,room_no,age,id)
     try:
         cursor.execute(udq)
         db.commit()
         return redirect(url_for('allusers'))
     except:
         db.rollback()
         return "Error in Query"
     
if __name__=="__main__":
    app.run()











   
    