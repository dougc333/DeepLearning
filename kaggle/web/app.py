import jinja2
import os
from flask import Flask, render_template


app = Flask(__name__)

def init():
    os.path.list


@app.route("/")
def main():
    return render_template("index.html",img_list=["../static/train/Type_1/700.jpg"])

if __name__=="__main__":
    app.run()