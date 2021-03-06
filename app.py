from flask import Flask, render_template, request
import json,urllib
data = []
dataJSON = urllib.request.urlopen("https://open.data.amsterdam.nl/Activiteiten.json").read()
data = json.loads(dataJSON.decode())

app = Flask(__name__)

@app.route('/hello/<name>')
def sayHello(name):
   return render_template("SayHello.html", name=name)

@app.route('/games')
def double():
   games = [
     {
         'naam': "Resident Evil 7: Biohazard",
         'bedrijf': 'Capcom',
         'urlplaatje': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNmZmZGM1NWYtYWUzNC00MWZmLTg2MTYtNDQzYmM3OWQxYmNlXkEyXkFqcGdeQXVyNDAzNzA0MzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg'
     },
     {
         'naam': "The Legend of Zelda: Breath of the Wild",
         'bedrijf': 'Nintendo Entertainment Planning & Development',
         'urlplaatje': 'https://images-na.ssl-images-amazon.com/images/I/81RbwMABstL._SL1455_.jpg'
     },
     {
         'naam': "Horizon Zero Dawn",
         'bedrijf': 'Guerrilla Games',
         'urlplaatje': 'http://vignette1.wikia.nocookie.net/horizonzerodawn/images/d/d4/Horizon-zero-dawn-box-art.jpg/revision/latest?cb=20160616210605'
     }
   ]
   games.append({ 'naam': 'sjaak'})
   return render_template("Games.html", spellen=games)

@app.route('/activiteiten')
def activiteiten():
    return render_template("Activiteiten.html", activiteiten=data)

@app.route('/films')
def films():
    films = ["The Matrix", "The Lion King", "Madagascar", "The Revenge of the Nerds"]
    return render_template("Films.html", filmlijst=films)

@app.route('/filminfo')
def filminfo():
    film = { "naam": "The Matrix", "jaar": 1999, "speelduur": 136, "opbrengst": 463517383 }
    return render_template("FilmInfo.html", filminfo=film)

@app.route('/')
def hoofdpagina():
    return render_template("index.html")

@app.route('/BerichtFormulier')
def BerichtFormulier():
    return render_template("BerichtFormulier.html")

@app.route('/VerwerkFormulier', methods=["POST"])
def VerwerkFormulier():
    naam = request.form['gebruikersnaam']
    mailadres = request.form['gebruikersemail']
    bericht = request.form['bericht']


    return render_template("VerwerkFormulier.html", name = naam, ma = mailadres, ber = bericht)


if __name__ == "__main__":
   app.run(debug=True)
