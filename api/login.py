from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests
from itsdangerous import JSONWebSignatureSerializer
import time

class Tel(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('phone', type=str)
        self.parser.add_argument('code', type=str)
        
    def post(self):
        args = self.parser.parse_args()
        phone = args['phone']
        code = args['code']
        s = JSONWebSignatureSerializer('secret-key')
        return s.dumps({'phone': phone, 'time':time.time()})


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Tel, '/login/tel')
    app.run(debug=True)