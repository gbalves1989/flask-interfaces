from pydantic import BaseModel, Field


class NoContentResponse(BaseModel):
    content: str = Field(description='no content')