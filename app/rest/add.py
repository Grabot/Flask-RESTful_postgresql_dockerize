from app import db
from app.rest import app_api
from flask_restful import Api
from flask_restful import Resource
from app.models.place_holder import PlaceHolder


class Add(Resource):

    def get(self, name):
        place_holder = PlaceHolder(name=name)
        db.session.add(place_holder)
        db.session.commit()
        return {
            'result': True,
            'message': 'Congratulations, you have just added an object in the database',
            'object': place_holder.serialize
        }

    def put(self, name):
        pass

    def delete(self, name):
        pass

    def post(self, name):
        pass


api = Api(app_api)
api.add_resource(Add, '/add/<string:name>', endpoint='add')
