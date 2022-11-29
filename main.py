from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def checkErrors():
  username = request.form['username']
  email = request.form['email']
  password = request.form['password']
  confirmPassword = request.form['confirmPassword']
  usernameError = ""
  emailError = ""
  passwordError = ""
  confirmPasswordError = ""
  errorCount = 0
  if username == "":
    usernameError = "This field needs to be filled out"
    errorCount += 1
  else:
    if " " in username:
      usernameError = "Username cannot have a space in it"
      errorCount += 1
    else:
      if len(username) < 3 or len(username) > 20:
        usernameError = "Username needs to be between 3 and 20             characters"
        errorCount += 1
  if email != "":
    if " " in email:
      emailError = "Email cannot have a space in it"
      errorCount += 1
    else:
      if "@" in email and "." in email:
        atCount = 0
        periodCount = 0
        for char in email:
          if char == "@":
            atCount += 1
        if atCount > 1:
          emailError = "There can only be one '@' in the email"
          errorCount += 1
        for char in email:
          if char == ".":
            periodCount += 1
        if periodCount > 1:
          emailError = "There can only be one '.' in the email"
          errorCount += 1
        if len(email) < 3 or len(email) > 20:
          emailError = "Email needs to be between 3 and 20                   characters"
          errorCount += 1
      else:
        emailError = "Email has to have '@' and '.' in it"
        errorCount += 1
  if password == "":
    passwordError = "This field needs to be filled out"
    errorCount += 1
  else:
    if " " in password:
      passwordError = "Password cannot have a space in it"
      errorCount += 1
    else:
      if len(password) < 3 or len(password) > 20:
        passwordError = "Password needs to be between 3 and 20             characters"
        errorCount += 1
      else:
        if password != confirmPassword:
          passwordError = "Passwords do not match"
          errorCount += 1
  if confirmPassword == "":
    confirmPasswordError = "This field needs to be filled out"
    errorCount += 1
  if errorCount > 0:
    return render_template(
      "index.html",
      usernameError = usernameError,
      emailError=emailError,
      passwordError=passwordError,
      confirmPasswordError=confirmPasswordError,
      username=username,
      email=email
    )
  else:
    return render_template(
      "welcome.html",
      username=username
    )
        
        

app.run(host='0.0.0.0', port=8080)
