from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

from courseRecommender import CourseRecommender

app = Flask(__name__)
api = Api(app)

class Courses(Resource):
    def get(self, input_string):
        userInput = input_string 
        #'python, machine learning, neural networks, artificial intelligence, regression, classification, modeling, supervised'
        recommender = CourseRecommender()
        result = recommender.recommendCourses(userInput)
        #{'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Recommend(Resource):
    def post(self):
        content = request.get_json(force=True)
        userInput = content['userInput']
        recommender = CourseRecommender()
        result = recommender.recommendCourses(userInput)
        print(result)
        return jsonify(result)

#@app.route('/recommend', methods=['POST'])

api.add_resource(Courses, '/courses/<input_string>') # Route_3
api.add_resource(Recommend, '/recommend') # Route_3

if __name__ == '__main__':
     app.run(port='5002')