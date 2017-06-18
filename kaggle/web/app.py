import jinja2
import os
from os import path,walk
from flask import Flask, render_template


app = Flask(__name__)
list_type1 = []

def init():
    list_f=[]
    print(os.getcwd())
    for dirpath, dirnames, filenames in walk(os.getcwd()+"/static/train/Type_1"):
        for f in filenames:
            if f!='.DS_Store':
                print(f)
                list_f.append (f)
        return list_f


@app.route("/")
def main():
    return render_template("index.html",img_list=list_type1)

if __name__=="__main__":
    list_type1.extend(init())
    app.run()