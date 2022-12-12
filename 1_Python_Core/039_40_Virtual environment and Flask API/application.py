from flask import Flask, render_template

app = Flask(__name__)     # __main__()

@app.route('/')
def index():
    return "Hello from first Flask App"

@app.route('/home')
def home():
    return "<h1>Hello from Home route</h1>"

@app.route('/profile')
def profile():
    goa = "we are going to goa this year"
    return render_template('index.html', name = goa)

if __name__ == '__main__':
    app.run(port=5000)


# localhost:5000
# 127.0.0.1:5000



#  API - Application Programming Interface

# API endpoint - URL

# https://www.google.co.in/search?q=python
# scheme     DNS            route  query-string
#            IP- IPv4 IPv6

# http
# https
# ftp
# file