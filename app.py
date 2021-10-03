# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

# creating the flask app
app = Flask(__name__)
app.url_map.strict_slashes = False

# creating an API object
api = Api(app)

with open('cuss_words.txt', 'r') as f:
    lines = [line.strip() for line in f]
    abuses = {'cuss_words': lines}

class Home(Resource):

    def get(self):
        return 'Invalid Request'

class abuseapi(Resource):

    def get(self):
        return jsonify(abuses)

class check(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q', type=str)
        args = parser.parse_args()
        if args['q'] in abuses['cuss_words']:
            return jsonify('True')
        else:
            return jsonify('False')


# adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(abuseapi, '/api/v1')
api.add_resource(check, '/api/v1/check')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
