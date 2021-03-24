from app.rest import app_api
from flask_restful import Api
from flask_restful import Resource
from app.models.place_holder import PlaceHolder


class All(Resource):

    def get(self):
        place_holders = PlaceHolder.query.all()
        return {
            "placeholder_list": [place.serialize for place in place_holders]
        }

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass


api = Api(app_api)
api.add_resource(All, '/all', endpoint='all')
