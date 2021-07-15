from flask import Flask
from flask_pymongo import PyMongo
import yaml

config_yaml = yaml.safe_load(open("../config/config.yaml"))

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://{}:{}@datafy.odhvq.mongodb.net/myFirstDatabase?retryWrites" \
                          "=true&w=majority".format(config_yaml.get("mongo_user"), config_yaml.get("mongo_password"))
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "<p>Connected</p>"


app.run(debug=True)
