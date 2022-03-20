"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,flash
from flask.helpers import send_from_directory
from app import app, db
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Prop
import os



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")



@app.route('/property', methods =['POST', 'GET'])
def properties():
    form = PropertyForm()
    if request.method=='POST':
        if form.validate_on_submit():
            propertyTitle = form.propertyTitle.data
            propertyDesc = form.propertyDesc.data
            no_of_bedrooms = form.no_of_bedrooms.data
            no_of_bathrooms = form.no_of_bathrooms.data
            price = form.price.data
            location = form.location.data
            propertyType = form.propertyType.data
            photo = form.photo.data
            filename =  secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            proprecord = Prop(
                        propertyTitle,
                        propertyDesc,
                        no_of_bedrooms,
                        no_of_bathrooms,
                        price,
                        location,
                        propertyType,
                        filename)
            db.session.add(proprecord)
            db.session.commit()

            flash('Property is added successfully','success')
            return redirect(url_for('Pproperties'))
        else: 
            flash_errors(form)
    return render_template('propertyForm.html', form=form)

@app.route('/properties')
def Pproperties():
    propert = Prop.query.all()
    return render_template('properties.html', propert=propert)

@app.route("/properties/<propertyid>")
def pid(propertyid):
    propertyid = Prop.query.filter_by(id=propertyid).first()
    return render_template('pid.html', propertyid=propertyid)

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

    
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
