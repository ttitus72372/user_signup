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
    Uerror = ""
    Perror = ""
    Verror = ""
    Eerror = ""
    



    if Username.strip() == "":
        Uerror = "Username is blank, you must input a Username."   
    elif " " in Username:
        Uerror = "There is a space in your Uername"
    elif len(Username) < 3 or len(Username) > 20:
        Uerror = "Your Username is either to short or to long, make sure it is between 3 and 20 characters long."
    
    if Password.strip() == "":
        Perror = "Passwrod is blank, you must set up a Password."
    elif len(Password) < 3 or len(Password) > 20:
        Perror = "Your password is either to short or to long, make sure it is between 3 and 20 characters long."
    elif " " in Password:
        Perror = "There is a space in your Password"

    if Verify.strip() == "":
        Verror = "You must verfiy your password!"
    elif Password != Verify:
        Verror = "You passwords do not macth!"   
     
    if Email.strip() != "":
        atsym = 0
        dot = 0
        for x in Email:
            if x == "@":
                atsym += 1
            if x == ".":
                dot += 1
        if atsym > 1 or atsym < 1:
            Eerror = "You have more than one at symbol or no at symbol in your email."
        elif dot > 1 or dot < 1:
            Eerror = "You have more than one dot symbol or no dot symbol in your email."
        elif " " in Email:
            Eerror = "There is a space in your email"
        elif len(Email) < 3 or len(Email) > 20:
            Eerror = "Your Email is either to short or to long, make sure it is between 3 and 20 characters long."
    return render_template('edit.html', User_error=Uerror, Pass_error=Perror, Verify_error=Verror,Email_error=Eerror)
        
            

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
