from flask import Flask
from flask_restful import Api
from api.route import set_api
from project import configs, database

app = Flask(__name__)
app.config.from_object(configs.config)

api = Api(app)

if __name__ == "__main__":
    set_api(api)
    app.run('localhost', 1472)


