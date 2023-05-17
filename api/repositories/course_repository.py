from api import db

from api.models.course_model import CourseModel
from api.entities.course_entity import CourseEntity
from api.interfaces.course_interface import CourseInterface


class CourseRepository(CourseInterface):
    def create(entity: CourseEntity) -> CourseModel:
        course_db: CourseModel = CourseModel(
            name=entity.name,
            description=entity.description
        )
        
        db.session.add(course_db)
        db.session.commit()
        return course_db
    
    def find_by_id(course_id: int) -> CourseModel:
        course_db: CourseModel = CourseModel.query.filter_by(id=course_id).first()
        return course_db
    
    def update(course_db: CourseModel, course_entity: CourseEntity) -> None:
        course_db.name = course_entity.name
        course_db.description = course_entity.description
        db.session.commit()
    
    def delete(course_db: CourseModel) -> None:
        db.session.delete(course_db)
        db.session.commit()
