from flask import Flask, request
from caesar import rotate_string

app = Flask('app')

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="POST">
        <label for="rot">Rotate by:
        <input type="text" name="rot" value="0" />
        <p class="error"></p>
        </label>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Encrypt Text" />
      </form>
    </body>
</html>
'''

@app.route('/')
def index():
    return form.format('')
@app.route('/', methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    return form.format(rotate_string(text, int(rot)))

app.run(host='0.0.0.0', port=8080)
