from flask import Flask
from flask_pymongo import PyMongo
import yaml
from rest.controllers.persons import persons_blueprint

config_yaml = yaml.safe_load(open("config/config.yaml"))

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://{}:{}@datafy.odhvq.mongodb.net/myFirstDatabase?retryWrites" \
                          "=true&w=majority".format(config_yaml.get("mongo_user"), config_yaml.get("mongo_password"))
mongo = PyMongo(app)
app.register_blueprint(persons_blueprint, url_prefix='/api/person')

if __name__ == '__main__':
    app.run()
