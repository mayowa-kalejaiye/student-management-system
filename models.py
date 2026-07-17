from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str
    score: int = Field(ge=0, le=100)  # Score must be between 0 and 100
