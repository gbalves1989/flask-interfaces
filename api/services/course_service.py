from flask import make_response, Response

from api.schemas.course_schema import CourseSchema
from api.entities.course_entity import CourseEntity
from api.models.course_model import CourseModel
from api.repositories.course_repository import CourseRepository
from api.routes.requests.course_request import CourseBody, CoursePath, CourseQuery
from api.utils.paginate import paginate
from api.utils.http_error_message import http_error_message


class CourseService:
    def create_course(request: CourseBody) -> Response:
        cs: CourseSchema = CourseSchema()
        
        course_entity: CourseEntity = CourseEntity(
            name=request.name,
            description=request.description
        )
        
        course_model: CourseModel = CourseRepository.create(course_entity)
        return make_response(cs.jsonify(course_model), 201)

    def list_courses(query: CourseQuery) -> Response:
        cs: CourseSchema = CourseSchema(many=True)
        return paginate(CourseModel, cs, query.page, query.per_page)
    
    def show_course(course_id: int) -> Response:
        course_db: CourseModel = CourseRepository.find_by_id(course_id)
        
        if course_db is None:
            return http_error_message('Course not found', 404)
        
        cs: CourseSchema = CourseSchema()
        return make_response(cs.jsonify(course_db), 200)
    
    def update_course(course_id: int, request: CourseBody) -> Response:
        course_db: CourseModel = CourseRepository.find_by_id(course_id)
        
        if course_db is None:
            return http_error_message('Course not found', 404)
    
        course_entity: CourseEntity = CourseEntity(
            name=request.name,
            description=request.description
        )
        
        CourseRepository.update(course_db, course_entity)
        course: CourseModel = CourseRepository.find_by_id(course_id)
        cs: CourseSchema = CourseSchema()
        return make_response(cs.jsonify(course), 202)
    
    def delete_course(course_id: int) -> Response:
        course_db: CourseModel = CourseRepository.find_by_id(course_id)
        
        if course_db is None:
            return http_error_message('Course not found', 404)
        
        CourseRepository.delete(course_db)
        return make_response({
            'content': 'Course removed with successfully'
        }, 204)
        