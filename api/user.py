
from main import app
from flask_restful import Api, Resource

class Login(Resource):
    def post(self):
        return 'response is ok'

class User(Resource):
    def get(self):
        return 'hello world'


api = Api(app)
api.add_resource(User, '/hello')
api.add_resource(Login, '/sns/login')

if __name__ == "__main__":
    app.run(debug=True)