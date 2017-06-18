import jinja2
import os
from os import path,walk
from flask import Flask, render_template
import sqlite3
from sqlite3 import connect

app = Flask(__name__)
list_type1 = []

def init():
    list_f=[]
    print(os.getcwd())
    for dirpath, dirnames, filenames in walk(os.getcwd()+"/static/train/Type_1"):
        for f in filenames:
            if f!='.DS_Store':
                #print(f)
                list_f.append (f)
        return list_f

def init_db():
    database_file = "images.db"
    conn = connect(database_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")

    rows = cur.fetchall()

    for row in rows:
        print(row)

@app.route("/")
def main():
    return render_template("index.html",img_list=list_type1,img_ht=100,img_width=100)

if __name__=="__main__":
    init_db()
    list_type1.extend(init())
    app.run()