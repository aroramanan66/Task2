from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
#Rendering to the index.html template  
@app.route("/")
def home():
    return render_template("index1.html")

#Performing the GET,POST operation 
@app.route("/login",  methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password1 = request.form["password"]
        file1=request.form["file"]
        return redirect(url_for("user",usr=user,passw=password1,fil=file1))
    else:
        return render_template("login.html")

#Display the values enter in the POST operation
@app.route("/<usr>/<passw>/<fil>")
def user(usr,passw,fil):
    return f"<h1> Name: {usr}</h1> <h2> Password: {passw}</h2> Image: {fil}"

if __name__ == "__main__":
    app.run(debug=True)
