# -*- coding: utf-8 -*-  

from flask import Flask
from flask_restful import Api, Resource


class User(Resource):
    def get(self):
        return 'hello user'


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(User, '/user')
    app.run(debug=True)