from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/add", methods=['POST'])
def signup():
    
    Username = request.form['username']
    Password = request.form['password']
    Verify = request.form['verify']
    Email = request.form['email']
        
    
    if Username.strip() == "":
        error = "Username is blank, you must input a Username."
        return redirect("/?error=" + error)

    if Password.strip() == "":
        error = "Passwrod is blank, you must set up a Password."
        return redirect("/?error=" + error)

    if Verify.strip() == "":
        error = "You must verfiy your password!"
        return redirect("/?error=" + error)
    
    if len(Username) < 3 or len(Username) > 20:
        error = "Your Username is either to short or to long, make sure it is between 3 and 20 characters long."
        return redirect("/?error=" + error)
    
    if len(Password) < 3 or len(Password) > 20:
        error = "Your password is either to short or to long, make sure it is between 3 and 20 characters long."
        return redirect("/?error=" + error)
    
    if " " in Username:
        error = "There is a space in your Uername"
        return redirect("/?error=" + error)

    if " " in Password:
        error = "There is a space in your Password"
        return redirect("/?error=" + error)

    if Password != Verify:
        error = "You passwords do not macth!"
        return redirect("/?error=" + error)
    if Email.strip() != "":
        atsym = 0
        dot = 0
        for x in Email:
            if x == "@":
                atsym += 1
            if x == ".":
                dot += 1
        if atsym > 1 or atsym < 1:
            E1error = "You have more than one @ symbol or no @ symbol in your email."
            return redirect("/?error=" + E1error)
        if dot > 1 or dot < 1:
            E2error = "You have more than one @ symbol or no @ symbol in your email."
            return redirect("/?error=" + E2error)
        if " " in Email:
            E3error = "There is a space in your email"
            return redirect("/?error=" + E3error)
        if len(Email) < 3 or len(Email) > 20:
            E4error = "Your Email is either to short or to long, make sure it is between 3 and 20 characters long."
            email_length = len(Email)
            return redirect("/?error=" + E4error + "The number of characters in your email is:" +str(email_length))

    Username_escaped = cgi.escape(Username, quote=True)
    Password_escaped = cgi.escape(Password, quote=True)
    VerifyPassword_escaped = cgi.escape(Verify, quote=True)
    Email_escaped = cgi.escape(Email, quote=True)

    return render_template('welcome.html',name=Username)

@app.route("/")
def index():
    Username = ""
    Email = ""
    encoded_error = request.args.get("error")
    return render_template('edit.html',Username=Username, Email=Email, error=encoded_error and cgi.escape(encoded_error, quote=True))




app.run()
