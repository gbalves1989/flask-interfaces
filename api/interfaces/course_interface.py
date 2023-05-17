from abc import ABC, abstractmethod

from api.models.course_model import CourseModel
from api.entities.course_entity import CourseEntity


class CourseInterface(ABC):
    @abstractmethod
    def create(entity: CourseEntity) -> CourseModel:
        pass
    
    @abstractmethod
    def find_by_id(course_id: int) -> CourseModel:
        pass
    
    @abstractmethod
    def update(course_db: CourseModel, course_entity: CourseEntity) -> None:
        pass
    
    @abstractmethod
    def delete(course_db: CourseModel) -> None:
        pass
