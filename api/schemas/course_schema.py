from api import ma
from marshmallow import fields

from api.models.course_model import CourseModel


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: CourseModel = CourseModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'description')
    
    name: str = fields.String(required=True)
    description: str = fields.String(required=True) 
