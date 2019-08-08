

from flask import Flask
from flask_restful import Api, Resource
import requests


class Login(Resource):
    def post(self):
        return 'response is ok'

class User(Resource):
    def get(self):
        r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
        print(r.status_code)
        return 'hello user'


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(User, '/user')
    app.run(debug=True)