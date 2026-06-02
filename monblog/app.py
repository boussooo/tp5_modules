from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    articles = [
        {"titre": "Python et Flask", "auteur": "Mame", "resume": "Un guide pratique pour créer des applications web avec Flask."},
        {"titre": "Bases de données", "auteur": "Awa", "resume": "Introduction aux bases de données relationnelles et leur utilisation."},
        {"titre": "Sécurité Web", "auteur": "Ibrahima", "resume": "Les bonnes pratiques pour sécuriser vos applications web."}
    ]
    return render_template("accueil.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
