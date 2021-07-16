from flask import request, Blueprint

persons_blueprint = Blueprint('person', __name__)


@persons_blueprint.route("/", methods=['POST'])
def create():
    from Server.app import mongo
    if request.headers.get('Content-Type') == 'application/json':
        print(request)
        new_person = request.json
        mongo.db.persons.insert_one(new_person)
        return {'result': new_person}
    return "Headers were not set accordingly", 400
