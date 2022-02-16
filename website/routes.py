import os
import secrets
import csv
from PIL import Image
from collections import Counter
from flask_mail import Message
from flask import Flask, render_template, url_for, flash, redirect, request, abort, send_file
from website.forms import SampleForm
from website.models import User, SampelModel
from website import app, db, bcrypt, mail
from flask_login import login_user, current_user, login_required

@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('index.html', title='Home')



@app.route("/sample_form", methods=['GET', 'POST'])
def contact():
    form = SampleForm()

    if form.validate_on_submit():

        return redirect(url_for('index'))
    return render_template('index.html', title='sample form', form=form)
