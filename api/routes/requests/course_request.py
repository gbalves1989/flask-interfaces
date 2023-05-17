from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os


load_dotenv()


class CoursePath(BaseModel):
    course_id: int = Field(description='course id')


class CourseBody(BaseModel):
    name: str = Field(min_length=5, max_length=100, description='course name')
    description: str = Field(min_length=5, max_length=180, description='course description')


class CourseQuery(BaseModel):
    page: int = Field(int(os.environ.get('PAGE_DEFAULT')), description='actual page')
    per_page: int = Field(int(os.environ.get('PER_PAGE_DEFAULT')), description='registers per page')
