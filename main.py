
from flask import Flask
from flask_restful import Api

from api import User
from api import Tel

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(Tel, '/login/tel')

if __name__ == "__main__":
    app.run(debug=True)
