from flask import Flask
from GestioneProdotto.GestioneProdottoControll import gu
app = Flask(__name__)

app.register_blueprint(gu)

if __name__ == '__main__':
    app.run()
