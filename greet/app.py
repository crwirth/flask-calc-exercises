from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    welcome = """
    <html>
        <body>
        <h1>Welcome</h1>
        </body>
    </html>
    """
    return welcome

@app.route('/welcome/home')
def welcome_home():
    welc_home = """
    <html>
        <body>
        <h1>welcome home</h1>
        </body>
    </html>
    """
    return welc_home

@app.route('/welcome/back')
def welcome_back():
    welc_back = """
    <html>
        <body>
        <h1>welcome back</h1>
        </body>
    </html>
    """
    return welc_back




