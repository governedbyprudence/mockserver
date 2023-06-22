from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/login",methods = ["POST"])
def login():
    username = "testuser@gmail.com"
    password = "123456"
    json = request.json

    if username == json["username"] and password == json["password"]:

        return {
            "token":"abcd"
        }
    
@app.route("/getdata")
def getData():
    token = request.headers.get("Authorization").split(" ")[-1]
    print(token)
    if(token == "abcd"):
        return{
        "data":"some valid data"
        }


if __name__ == '__main__':
   app.run()
