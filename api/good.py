# -*- coding: utf-8 -*-  
from flask import Flask
from flask_restful import Api, Resource, reqparse
from database.mongo import client
from bson import json_util
import json


class List(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('cat_id', type=str)
        self.db = client["main"]
        super(List, self).__init__()
    
    def post(self):
        args = self.parser.parse_args()
        cat_id = args['cat_id']

        if cat_id is None:
            return {'message':'参数错误'}, 1001
        if len(cat_id) == 0:
            return {'message':'参数错误'}, 1001
        
        category = self.db['category']
        goods_id = category.find_one({'cat_id':cat_id}, {'goods': 1, '_id': 0})
        ids = json.loads(json_util.dumps(goods_id))['goods']
        good = self.db['good']
        return {'message':'成功', 'data':json_util.dumps(good.find({'id': { '$in': ids }}, {'_id':0}))}, 200


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(List, 'good/list')
    app.run(debug=True)