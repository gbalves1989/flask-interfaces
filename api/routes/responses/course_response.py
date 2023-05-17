from pydantic import BaseModel, Field


class CourseResponse(BaseModel):
    id: int = Field(description='course id')
    name: str = Field(description='course name')
    description: str = Field(description='description of course')


class CourseListResponse(BaseModel):
    total: int = Field(description='total of courses')
    pages: int = Field(description='number of pages')
    next: int = Field(description='next page')
    prev: int = Field(description='preview page')
    results: list[CourseResponse]
