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
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)