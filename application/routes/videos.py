from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse, abort

from ..schema import videosSchema
from ..models.video import Video
from .. import db

videos = Blueprint('videos', __name__)


@videos.route("/videos/<video_id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
def videos_route(video_id):
    if request.method == 'GET':
        video:Video = Video.query.filter_by(id=video_id).first()
        return videosSchema.video_schema.dump(video), 200

    if request.method == 'PUT':
        video = Video(
            name=request.json['name'], 
            views=request.json['views'], 
            likes=request.json['likes'])
        db.session.add(video)
        db.session.commit()
        return videosSchema.video_schema.dump(video), 201

    if request.method == 'DELETE':
        video:Video = Video.query.filter_by(id=video_id).first()
        db.session.delete(video)
        return '', 204