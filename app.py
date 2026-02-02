from flask import Flask, render_template, request
import conexion_bdd

app = Flask(__name__)

@app.route("/getmail", methods=["GET", "POST"])
def getmail():
    resultat = None
    error = None

    if request.method == "POST":
        nom = request.form.get("nom").capitalize()

        conexion, cursor = conexion_bdd.conectar_bdd()
        email = conexion_bdd.consulta_email(cursor, nom)

        if email:
            resultat = email[0]
        else:
            error = "Aquest nom no existeix a la base de dades."

        cursor.close()
        conexion.close()

    return render_template("getmail.html", resultat=resultat, error=error)


@app.route("/addmail", methods=["GET", "POST"])
def addmail():
    missatge = None

    if request.method == "POST":
        nom = request.form.get("nom").capitalize()
        email = request.form.get("email")

        conexion, cursor = conexion_bdd.conectar_bdd()
        conexion_bdd.insertar_email(conexion, cursor, nom, email)
        cursor.close()
        conexion.close()

        missatge = "Correu afegit correctament."

    return render_template("addmail.html", missatge=missatge)
