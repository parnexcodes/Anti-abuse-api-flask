# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

# creating the flask app
app = Flask(__name__)
app.url_map.strict_slashes = False


# function to get file contents
def get_content(filepath):
    with open(filepath, 'r') as f:
        lines = set()       # using sets to avoid duplicate enteries
        for line in f:
            lines.add(line.strip())
    return {'cuss_words': list(lines)}


# creating an API object
api = Api(app)


class Home(Resource):

    def get(self):
        return 'Invalid Request'

class abuseapi(Resource):

    def get(self):
        abuses = get_content("cuss_words.txt")
        return jsonify(abuses)

class check(Resource):

    def get(self):
        abuses = get_content("cuss_words.txt")
        parser = reqparse.RequestParser()
        parser.add_argument('q', type=str)
        args = parser.parse_args()
        if args['q'] in abuses['cuss_words']:
            return jsonify(True)
        else:
            return jsonify(False)


# adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(abuseapi, '/api/v1')
api.add_resource(check, '/api/v1/check')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
