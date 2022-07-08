from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
api = Api(app)
app.config.from_object(config.DevelopmentConfig)
db = SQLAlchemy(app)
db.create_all()

#basic get and post
names = {"sai": {"age": 19, "gender": "male"},
            "bill": {"age": 23, "gender": "male"}}
class HelloWorld(Resource):
    def get(self, name, numb):
        return names[name]

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:numb>")

# getting larger data
pictures = {}
class picture(Resource):
    def get(self, picture_id):
        return pictures[picture_id]

    def put(self, picture_id):
        print(request.form['likes'])
        pass

api.add_resource(picture, "/picture/<int:picture_id>")

# reqparse
video_put_args = reqparse.RequestParser() # make new request parser object to make sure it fits the correct guidelines
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views on the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

videos = {}

def abort_if_id_invalid(video_id):
    if video_id not in videos:
        abort('Video id is not valid...')

def abort_if_id_valid(video_id):
    if video_id in videos:
        abort('ZThis already exists with that ID...')

class Video(Resource):
    def get(self, video_id):
        abort_if_id_invalid(video_id=video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_id_valid(video_id=video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_id_invalid(video_id=video_id)
        del videos[video_id]
        return '', 204

if __name__ == "__main__":
    app.run(debug=True)