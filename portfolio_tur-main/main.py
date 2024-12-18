from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class FeedBack (db.Model):
    email=db.Column(db.String(90),nullable=False)
    note=db.Column(db.String(300),nullable=False)
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)


# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    email=request.form.get('email')
    text=request.form.get('text')
    if text:
        fd=FeedBack(email=email,note=text)
        db.session.add(fd)
        db.session.commit()
    button_python = request.form.get('button_python')
    button_discord=request.form.get('button_discord')
    button_html=request.form.get('button_html')
    button_db=request.form.get('button_db')
    return render_template('index.html', button_python=button_python,
                           email=email,
                           text=text,
                           button_db=button_db,
                           button_discord=button_discord,
                           button_html=button_html)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
