from flask import Flask, render_template, flash, request, url_for

app = Flask(__name__)


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/dashboard/')
def dashboard():
    return("hi")
    #return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")

@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('home'))
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error = error)

if __name__ == '__main__':
    app.run()




