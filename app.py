from flask import Flask,render_template,request
import requests




# Initialize the Flask application
app = Flask(__name__)

@app.route("/login",methods=["POST"])
def receive_data():
    name = request.form.get('username')
    password = request.form.get('password')
    return f"Name: {name}, Password: {password}"
    

@app.route('/')
<<<<<<< HEAD
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
=======
def hello_world():
    return render_template("login.html")
>>>>>>> b06ad2e4dc2cafa6d921e669b3c1f84ef9efc609


if __name__ == '__main__':
    app.run(debug=True)