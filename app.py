from flask import Flask
from flask import render_template, request, url_for, redirect
#from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.utils import redirect

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/tasks.db'
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

db.create_all()

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html',tasks = tasks)

@app.route('/create-task',methods=['POST'])
def create():
    content = request.form['titulo']
    done = False
    task = Task(content=content,done=done)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<int:id>')
def done(id):
    task = Task.query.filter_by(id=id).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)