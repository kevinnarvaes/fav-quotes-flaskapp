from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#for rendering templates with flask
#First letter must be uppercase
app = Flask(__name__) #The name of the application name or package
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:Alucinante123*@localhost/quotes'
#^^For connection to local server
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xnfwvewfmxmznu:ac00ef66979ddf2b96d08da121684bedf5c51e5c6a81595df1c6f8bf23c0d6fe@ec2-52-72-252-211.compute-1.amazonaws.com:5432/ddrvi3khou5a3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#^^Event notification in SQLALchemy to track modifications

db = SQLAlchemy(app)

class Favquotes(db.Model):
    #Defines class for db and it's data validations
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


# End points
@app.route('/')
def index():
    result = Favquotes.query.all() #Queries all records inside this table
    return render_template('index.html', result = result)
# You can inject variables into a html

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods =  ['POST']) #We have to set the type request in order to save info
def process():
    #create variables to capture data
    author = request.form['author'] #captures the answers of the form
    quote = request.form['quote']
    quotedata = Favquotes(author = author, quote = quote) #saves parameters from form
    db.session.add(quotedata) #adds data to the session of the db
    db.session.commit() #saves changes to the database
    return redirect(url_for('index'))
#Rendering templates. Flask looks for them in a folder named tamplates