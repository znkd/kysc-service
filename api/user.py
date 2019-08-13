

from flask import Flask
from flask_restful import Api, Resource
import requests


class Login(Resource):
    def get(self):
        params = {'phone':'123', 'password':'111111'}
        r = requests.post('http://47.94.1.127:8010/sns/login', json=params)
        print(r.status_code)
        print(r.json())
        return r.json()

class User(Resource):
    def get(self):
        return 'hello user'


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(Login, '/login')
    app.run(debug=True)