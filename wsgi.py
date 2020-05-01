from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

from courseRecommender import CourseRecommender

application = Flask(__name__)

@application.route("/recommend", methods=['POST'])
def recommend():
    content = request.get_json(force=True)
    userInput = content['userInput']
    recommender = CourseRecommender()
    result = recommender.recommendCourses(userInput)
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    application.run()