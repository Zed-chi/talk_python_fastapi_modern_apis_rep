from pydantic import BaseModel


class Location(BaseModel):
    city: str


class Units:
    title: str
