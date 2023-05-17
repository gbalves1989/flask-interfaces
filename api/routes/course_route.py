from api import app 
from flask_openapi3 import APIBlueprint, Tag

from api.routes.requests.course_request import CoursePath, CourseBody, CourseQuery
from api.services.course_service import CourseService
from api.routes.responses.course_response import CourseResponse, CourseListResponse
from api.routes.responses.error_response import ErrorsResponse
from api.routes.responses.no_content_response import NoContentResponse


tag: Tag = Tag(name='Courses', description='List of routes')
api_courses: APIBlueprint = APIBlueprint(
    'courses',
    __name__,
    url_prefix='/courses',
    abp_tags=[tag]
)


@api_courses.post(
    '/',
    summary='Create a new course',
    description='Responsible to create and return a new course',
    responses={'201': CourseResponse}
)
async def store(body: CourseBody):
    return CourseService.create_course(body)


@api_courses.get(
    '/',
    summary='Return a list of courses',
    description='Responsible to return a list of courses',
    responses={'200': CourseListResponse}
)
async def index(query: CourseQuery):
    return CourseService.list_courses(query)


@api_courses.get(
    '/<int:course_id>',
    summary='Return some course by id',
    description='Responsible to return some course by id',
    responses={
        '200': CourseResponse,
        '404': ErrorsResponse
    }
)
async def show(path: CoursePath):
    return CourseService.show_course(path.course_id)


@api_courses.put(
    '/<int:course_id>',
    summary='Update the data course by id',
    description='Responsible to update the data course by id',
    responses={
        '202': CourseResponse,
        '404': ErrorsResponse
    }
)
async def update(path: CoursePath, body: CourseBody):
    return CourseService.update_course(path.course_id, body)


@api_courses.delete(
    '/<int:course_id>',
    summary='Remove some course by id',
    description='Responsible to remove some course by id',
    responses={
        '204': NoContentResponse,
        '404': ErrorsResponse
    }
)
async def delete(path: CoursePath):
    return CourseService.delete_course(path.course_id)

app.register_api(api_courses)
