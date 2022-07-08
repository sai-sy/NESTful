from .. import ma
from ..models.video import Video

class VideoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Video
    id = ma.auto_field()
    name = ma.auto_field()
    views = ma.auto_field()
    likes = ma.auto_field()

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)