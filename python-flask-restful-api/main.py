from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

names = {
    "tim": {
        "age": 19,
        "gender": "male"},
    "bill": {
        "age": 70,
        "gender": "male"}}
videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video is required.", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video")
video_put_args.add_argument("likes", type=str, help="Likes of the video")


class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self, name, age, gender):
        pass


def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")


class Video(Resource):

    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


# Routes
api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
