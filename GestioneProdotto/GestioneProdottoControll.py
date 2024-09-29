from flask import Flask, Blueprint, request, render_template
from GestioneAdmin.AdminDAO import AdminDAO
from GestioneProdotto.Prodotto import Prodotto
gu = Blueprint('gu', __name__, template_folder="gestioneUtente")

@gu.route('/Carica Prodotto', methods=['GET', 'POST'])
def CaricaProdotto():
    if request.method == 'GET':
        return render_template("CreateProdotto.html")
    if request.method == 'POST':
        nome = request.form['nome']
        descrizione = request.form['descrizione']
        prezzo = request.form['prezzo']

        prodotto = Prodotto(id = 0,  nome = nome, descrizione = descrizione, prezzo = prezzo)
        print(prodotto.get_nome())
        print(prodotto.get_descrizione())
        print("PPPPPPPPPPPPPProdotto: " + str(prodotto.get_prezzo()))
        admin = AdminDAO()
        admin.CreateProdotto(prodotto)

        return render_template("CreateProdotto.html")
