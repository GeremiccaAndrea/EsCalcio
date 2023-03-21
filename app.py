from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/squadraPreferita')
def squadraPreferita():
    return render_template('squadrapreferita.html')

@app.route('/formazioneMilan')
def formazioneMilan():
    return render_template('formazioneMilan.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)