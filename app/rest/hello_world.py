from app.rest import app_api
from flask_restful import Api
from flask_restful import Resource


class HelloWorld(Resource):

    def get(self):
        return {"Hello": "World"}

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass


api = Api(app_api)
api.add_resource(HelloWorld, '/', endpoint='hello_world')
