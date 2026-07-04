from flask import Flask

app = Flask(__name__)

#Bad Way
@app.route('/')
def welcome():
    return "<html><h1>Welcome to the Flask course</h1></html>"

if __name__ == '__main__':
    app.run(debug=True)
    
#Good Way
from flask import Flask, render_template
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)