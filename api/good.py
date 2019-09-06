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

class Detail(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str)
        self.db = client["main"]
        self.good_id = -1
        self.title = "title"
        self.subtitle = "subtitle"
        self.moneytype = 0
        self.goodpricecomment = "商品价格描述"
        self.goodimageurl = "" 
        super(Detail, self).__init__()
        pass

    def post(self):
        args = self.parser.parse_args()
        goods_id = args['id']
        if goods_id is None:
            #没有goods_id 或者 goods_id为无效值
            return ''
        goods_id = int(goods_id)
        good_detail_table = self.db['good_detail']
        single_good_detail = good_detail_table.find_one({'id':goods_id})
        single_goodJSON = json.loads(json_util.dumps(single_good_detail))
        return single_goodJSON

if __name__ == "__main__":
    #使用 curl http://localhost:5000/good/detail -d "id=22"
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(List, 'good/list')
    app.run(debug=True)