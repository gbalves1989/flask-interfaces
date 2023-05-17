from pydantic import BaseModel, Field


class ErrorsResponse(BaseModel):
    message: str = Field(description='error message')