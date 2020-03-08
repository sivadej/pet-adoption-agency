from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

from models import db, connect_db, Pet

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

@app.route('/<int:id>')
def show_pet_detail(id):
    pet = Pet.query.get_or_404(id)
    return render_template('pet_show_detail.html', pet=pet)

@app.route('/<int:id>/edit', methods=['POST','GET'])
def edit_pet_detail(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash('updated')
        return redirect('/')
    else:
        return render_template('pet_edit.html', pet=pet, form=form)