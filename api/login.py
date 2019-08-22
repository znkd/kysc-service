# -*- coding: utf-8 -*-  
from flask import Flask
from flask_restful import Api, Resource, reqparse
from itsdangerous import JSONWebSignatureSerializer
import time

class Tel(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('phone', type=str)
        self.parser.add_argument('code', type=str)
        super(Tel, self).__init__()
        
    def post(self):
        args = self.parser.parse_args()
        phone = args['phone']
        code = args['code']

        if phone is None or code is None:
            return {'message':'参数错误'}, 1001
        if len(phone) == 0 or len(code) == 0:
            return {'message':'参数错误'}, 1001
        
        s = JSONWebSignatureSerializer('secret-key')
        return {'message':'成功', 'token':s.dumps({'phone': phone, 'time':time.time()})}, 200


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Tel, '/login/tel')
    app.run(debug=True)