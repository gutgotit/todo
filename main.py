from flask import Flask, render_template,request,flash,redirect
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from time import time, ctime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///final.db"
app.config['SECRET_KEY']='fds,lfhsjdfhjmndfsm,gfg'
db=SQLAlchemy(app)
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    detail = db.Column(db.String(12), nullable=True)
    state = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime,default=datetime.now(), nullable=False)
class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False,unique=True)
    password=db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    date = db.Column(db.DateTime,default=datetime.now(), nullable=False)
@app.route('/home')
def home():
	tasks=Todo.query.filter_by().all()
	t = time()
	z=ctime(t)
	return render_template('index.html',time=z,tasks=tasks)
@app.route('/check/<int:post_slug>', methods = ['GET', 'POST'])
def check(post_slug):
		try:
			#print(post_slug)
			i=Todo.query.filter_by(sno=post_slug).first()
			if i.state ==1:
				j=0
			else:
				j=1
			Todo.query.filter(Todo.sno == i.sno).delete()
			entry = Todo(date=datetime.now(),sno=i.sno,title=i.title,detail=i.detail,state=j)
			db.session.add(entry)
			db.session.commit()
			return redirect('/home')
		except:
			return render_template('error.html')
		return redirect('/home')
@app.route('/', methods = ['GET', 'POST'])
def login():
	if(request.method=='POST'):
		try:
			name=request.form.get('name')
			password=request.form.get('pass')
			if name=='usman':
				if password=='usman14pro':
					return redirect('/home')
				else:
					return render_template('error.html')
			else:
				return render_template('error.html')
		except:
			return render_template('error.html')
	return render_template('login.html')
'''@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	
	if(request.method=='POST'):
		try:
			name=request.form.get('name')
			email=request.form.get('email')
			password=request.form.get('password')
			password2=request.form.get('password2')
			if password==password2:
				entry = Users(date=datetime.now(),name=name, email=email, password=password)
				db.session.add(entry)
				db.session.commit()
				return redirect('/')
			else:
				return render_template("error.html")
		except:
			return render_template("error.html")
	return render_template('signin.html')'''
@app.route('/add', methods = ['GET', 'POST'])
def add():
	if(request.method=='POST'):
		try:
			title=request.form.get('title')
			description=request.form.get('des')
			entry = Todo(date=datetime.now(),title=title,detail=description,state=0)
			db.session.add(entry)
			db.session.commit()
			return redirect('/home')
		except:
			return render_template("error.html")
	return render_template('add.html')
@app.route('/quotes')
def quotes():
	return render_template('quotes.html')
@app.route('/delete')
def delete():
	os.remove('final.db')
	db.create_all()
	return redirect('/home')


app.run()
                                                    