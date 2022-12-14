from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# Model for video.
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Video(name = {VideoModel.name}, views = {VideoModel.views}, likes = {VideoModel.likes})"


db.create_all()

# Parser for incoming data.
video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video is required.", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video")
video_put_args.add_argument("likes", type=str, help="Likes of the video")

video_update_args = reqparse.RequestParser()
video_update_args.add_argument(
    "name", type=str, help="Name of the video is required.", required=True)
video_update_args.add_argument("views", type=str, help="Views of the video")
video_update_args.add_argument("likes", type=str, help="Likes of the video")

# model for database.
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(video_id)
        if not result:
            abort(404, message="Video not found!")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.get(video_id)
        if result:
            abort(409, message="video id taken...")

        video = VideoModel(
            id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()

        return f"data added to db. {video}", 201

    def patch(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel.query.get(video_id)
        if not video:
            abort(404, "There isn't any video file.")

        if "name" in args:
            VideoModel.name = args['name']

    def delete(self, video_id):
        video = VideoModel.query.get(video_id)
        if not video:
            abort(404, "There isn't any video file.")
        db.session.delete(video)
        db.session.commit()
        return 200


# Routes
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
