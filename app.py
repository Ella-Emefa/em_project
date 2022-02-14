from flask import Flask, render_template, url_for, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import send_from_directory, abort
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
db = SQLAlchemy(app)
admin = Admin(app)

bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'a secret key is needed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////admin.db'
app.config['SECRET_KEY'] = 'my secret key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

admin.add_view(ModelView)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=80)],
                             render_kw={"placeholder": "password"})
    # is_admin = "admin";
    submit = SubmitField("Register")


def validate_username(self, username):
    existing_username = User.query.filter_by(
        username=username.data).first()
    if existing_username:
        raise ValidationError(
            "This user is not authorized to perform this action. Please contact your administrator."
        )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                       Length(min=4, max=20)],
                           render_kw={"placeholder": "username"})

    password = PasswordField(validators=[InputRequired(),
                                         Length(min=4, max=80)],
                             render_kw={"placeholder": "password"})
    submit = SubmitField("Login")




@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       user= User.query.filter_by(username=form.username.data).first()
       if user:
           if bcrypt.check_password_hash(user.password, form.password.data):
               login_user(user)
               return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


"""
string:
float:
int:
path:
uuid:
"""

app.config['STATIC_CSV'] = "C:/Users/USER/PycharmProjects/EM project/static/csv"

@app.route("/get-csv/<path:path>")
def get_csv(path):

    try:
        return send_from_directory(app.config['STATIC_CSV'], path=path, as_attachment=True)

    except FileNotFoundError:
        abort(404)

app.config['STATIC_CSV_ADMIN'] = "C:/Users/USER/PycharmProjects/EM project/static/csv/csv_admin"

@app.route("/get-csv admin/<path:path>")
def get_csv_admin(path):

    try:
        return send_from_directory(app.config['STATIC_CSV ADMIN'], path=path, as_attachment=True)

    except FileNotFoundError:
        abort(404)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    return render_template('dashboard.html')



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)






