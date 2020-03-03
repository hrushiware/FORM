from flask import Flask, request, render_template,redirect,url_for

app = Flask(__name__)



@app.route('/',methods=["POST","GET"])
def login():
    if request.method=="POST":
        name= request.form["name1"]
        age=request.form["age"]
        return render_template("user.html" ,name=name,age=age)
    else:
        return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)