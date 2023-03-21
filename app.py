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
    if squadre == "Napoli":       #si prende la variabile scritta nell' HTML
        return render_template("Napoli.html")
    elif squadre == "Roma": 
        return render_template("Roma.html")
    elif squadre == "Inter":
        return render_template("Inter.html")
    elif squadre == "Juve":
        return render_template('Juve.html')
    else:
        return render_template('Milan.html')

@app.route('/formazioneMilan')
def formazioneMilan():
    return render_template('formazioneMilan.html')

@app.route('/formazioneInter')
def formazioneInter():
    return render_template('formazioneInter.html')

@app.route('/formazioneRoma')
def formazioneRoma():
    return render_template('formazioneRoma.html')

@app.route('/formazioneNapoli')
def formazioneNapoli():
    return render_template('formazioneNapoli.html')

@app.route('/formazioneJuve')
def formazioneJuve():
    return render_template('formazioneJuve.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)