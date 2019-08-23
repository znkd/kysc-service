# -*- coding: utf-8 -*-  

from flask import Flask
from flask_restful import Api

from api.user import User
from api.login import Tel
from api.good import List



app = Flask(__name__)
api = Api(app)

api.add_resource(Tel, '/login/tel')
api.add_resource(User, '/user')
api.add_resource(List, '/good/list')

if __name__ == "__main__":
    app.run(debug=True)
