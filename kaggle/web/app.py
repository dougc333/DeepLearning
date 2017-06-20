import jinja2
import os
import json
from os import path,walk
from flask import Flask, render_template,request
import sqlite3
from sqlite3 import connect

app = Flask(__name__)

list_type1 = []
list_type2 = []
list_type3 = []

def init_type1():
    list_type1=[]
    for dirpath, dirnames, filenames in walk(os.getcwd()+"/static/train/Type_1"):
        for f in filenames:
            if f!='.DS_Store':
                #print(f)
                list_type1.append (f)
        return list_type1

def init_type2():
    list_type2=[]
    for dirpath, dirnames, filenames in walk(os.getcwd()+"/static/train/Type_2"):
        for f in filenames:
            if f!='.DS_Store':
                #print(f)
                list_type2.append (f)
        return list_type2

def init_type3():
    list_type3=[]
    for dirpath, dirnames, filenames in walk(os.getcwd()+"/static/train/Type_3"):
        for f in filenames:
            if f!='.DS_Store':
                #print(f)
                list_type3.append (f)
        return list_type3



def init_db():
    database_file = "images.db"
    conn = connect(database_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")

    rows = cur.fetchall()

    for row in rows:
        print(row)



@app.route('/test')
def checklist():
    row_values = [1, 2, 3, 4]
    all_tags = []

    for rownum in range(1,3):
        all_tags.append(row_values[1])

    return render_template('test.html', tags=all_tags)

@app.route('/signUp')
def signUp():
    print ("signUp")
    return render_template('signUp.html')


@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    print ("signUpUser")
    user =  request.form['username'];
    password = request.form['password'];
    print('user:',user)
    print('password:',password)
    return json.dumps({'status':'OK','user':user,'pass':password});

@app.route("/type1")
def type1():
    return render_template("type1.html",img_list1=list_type1,img_ht=300,img_width=300)

@app.route("/type2")
def type2():
    return render_template("type2.html", img_list2=list_type2,img_ht=300,img_width=300)

@app.route("/type3")
def type3():
    return render_template("type3.html", img_list3=list_type3,img_ht=300,img_width=300)



if __name__=="__main__":
    init_db()
    list_type2.extend(init_type2())
    list_type3.extend(init_type3())
    list_type1.extend(init_type1())
    app.run()