from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/task1.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class datosVideo(db.Model):
    __tablename__='datosVideo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200), nullable=True)
    #def __repr__(self):
    #    return '<datosVideo %r>' %self.title
db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/datos', methods=['POST'])
def editar():
    title = request.form['titulo']
    description = request.form['descripcion']
    task = datosVideo(title=title,description=description)
    db.session.add(task)
    db.session.commit()
    return render_template('index.html',title=title,description=description)
@app.route("/a")
def muestra():
    return render_template('muestra.html')
if __name__=='__main__':
    app.run(debug=True)