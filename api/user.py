

from flask import Flask
from flask_restful import Api, Resource
import urllib2
import urllib


class Login(Resource):
    def post(self):
        return 'response is ok'

class User(Resource):
    def get(self):
        return 'hello world'


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(User, '/user')
    app.run(debug=True)