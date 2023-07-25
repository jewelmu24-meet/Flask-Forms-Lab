from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "jewel.muk"
password = "36912"
facebook_friends=["Sabrina","Sarah","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		user= request.form['username']
		p=request.form['password']

		if user== username and p==password:
			return redirect(url_for('home'))

		else:
			return render_template('login.html')

	else:
		return render_template('login.html')



@app.route('/home')
def home():
	#return render_template('home.html')

 return render_template('home.html', face=facebook_friends)



@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	if name in facebook_friends:
		friends = True
	else:
		friends= False
	return render_template('friend_exists.html', friends=friends, name=name)



# Dynamic Routing Example
# @app.route('/home/<string:student>')
# def home(student):
# 	return render_template('home.html', name = student, face=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)