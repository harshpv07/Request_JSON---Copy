from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

from collections import defaultdict
mess = [] #This global list is used to store all the messages in the correct order

@app.route('/' , methods= ["GET" , "POST"]) #Login & Registration page
def homee():    
    return render_template("authen.html" ) #This page contains the login and registration page.


@app.route('/<name>' , methods= ["GET" , "POST"]) #Chat page
def index(name):    
    return render_template("home.html" , name = str(name)) #This page renders the chat window


@app.route('/message' , methods= ["GET" , "POST"]) #Insert message to buffer
def message(): 
    data = request.json #Fetch the request that contains the name of the sender and the message associated with it in JSON format
    mess.append(data) #Add the message and the sender name to the list
    print(data)
    return "" #We do send any response back to client since it is an insertion operation

@app.route('/getupdate' , methods= ["GET" , "POST"]) #Fetch all message from buffer
def getupdate():
    return jsonify(mess) #This will return the list of messages as response

app.run(debug=True)

