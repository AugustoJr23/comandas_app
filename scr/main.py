from flask import Flask
from settings import HOST, PORT, DEBUG

app = Flask(__name__)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)