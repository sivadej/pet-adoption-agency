from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

from models import db, connect_db, Pet #YourModel, #YourModel2, etc.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petdb'
app.config['SECRET_KEY']='YOUR_SECRET_KEY'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_index():
    pets = Pet.query.all()
    return render_template('pets_all.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        db.session.add(Pet(name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data))
        db.session.commit()

        flash(f'new pet added')
        return redirect('/add')
    else:
        return render_template('pets_add_new.html', form=form)