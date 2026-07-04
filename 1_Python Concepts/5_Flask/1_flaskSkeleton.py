from flask import Flask

# This creates the WSGI application instance
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask course"

if __name__ == '__main__':
    app.run()
