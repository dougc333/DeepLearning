from flask import Flask, render_template
app = Flask(__name__,static_folder='../kaggle/train/Type_1')


@app.route("/")
def main():
    return render_template("index.html")

if __name__=="__main__":
    app.run()