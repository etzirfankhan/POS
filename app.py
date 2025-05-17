from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired

#------------------------------Initialize flask app------------------------------------------------------
app = Flask(__name__)
app.secret_key = 'Key for securely sending and receiving data'


#-------------------------------Creating login form class-------------------------------------------------
class Login(FlaskForm):
    name = StringField(label="Name",render_kw={'placeholder':'Name'},validators=[InputRequired()])
    password = PasswordField(label='Password',render_kw={'placeholder':'Password'},validators=[InputRequired()])
    save = BooleanField(label='Remember Password?___')
    submit = SubmitField(label='Login')

#----------------------------------Routing login form to users-----------------------------------------------
@app.route("/", methods = ['post','get'])
def login_page():
    login_form = Login()
    if login_form.validate_on_submit():
        return render_template('home.html')
    return render_template('login.html',form = login_form)


#-------------------------------Redirecting users to homepage after login page---------------------------
@app.route('/home',methods = ['post'])
def homepage():
    return render_template('home.html')








if __name__ == '__main__':
    app.run(debug=True)