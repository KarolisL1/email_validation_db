from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_email', methods=["POST"])
def create_email():
    Email.save_email(request.form)
    return redirect('/emails')

@app.route('/emails')
def emails():
    email = Email.all()
    return render_template('success.html', email=email)

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/success')