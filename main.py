
from flask import Flask
from flask_restful import Api
from api import User
from api import Login

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(Login, '/login')

if __name__ == "__main__":
    app.run(debug=True)
