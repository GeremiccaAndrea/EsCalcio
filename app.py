from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login' , methods = ["GET"])
def login():
     
     return render_template('login.html')

@app.route('/squadraPreferita', methods = ["GET"])
def squadraPreferita():
    squadre = request.args.get("squadra") #si prende la variabile scritta nell' HTML
    print(squadre)
    if squadre == "Napoli": #si prende la variabile scritta nell' HTML
        return render_template("squadrapreferitaNapoli.html")
    else:
        return render_template('squadrapreferitaMilan.html')

@app.route('/formazioneMilan')
def formazioneMilan():
    return render_template('formazioneMilan.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)