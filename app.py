from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

from collections import defaultdict
mess = []

@app.route('/' , methods= ["GET" , "POST"]) #Home route
def homee():    
    return render_template("authen.html" ) #Render the page which contains the form details.


@app.route('/<name>' , methods= ["GET" , "POST"]) #Home route
def index(name):    
    return render_template("home.html" , name = str(name) , chathis = mess) #Render the page which contains the form details.


@app.route('/message' , methods= ["GET" , "POST"]) #Second route
def message(): #This is the message route where the we post the user details.
    data = request.json #Fetch the request whose body contains all the user details in JSON format
    mess.append(data)
    print(mess)
    print(data) #Print the user details in JSON format
    return "hey"

@app.route('/getupdate' , methods= ["GET" , "POST"]) #Second route
def getupdate(): #This is the message route where the we post the user details.
    return jsonify(mess)

app.run(debug=True)