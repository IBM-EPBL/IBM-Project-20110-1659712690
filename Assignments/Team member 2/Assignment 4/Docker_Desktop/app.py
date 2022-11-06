from flask import Flask,render_template
import os

doc_desk = Flask(__name__)

@doc_desk.route("/")
def index():
   return render_template("index.html")


if __name__=="__main__":
   port =os.environ.get("PORT",5000)
   doc_desk.run( host="0.0.0.0",port=port)