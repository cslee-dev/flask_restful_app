from flask import Flask
from flask_restful import Api
from project import configs, database

app = Flask(__name__)
app.config.from_object(configs)
api = Api(app)

from api import route

if __name__ == "__main__":
    app.run('localhost', 1472)


