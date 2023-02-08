from datetime import datetime

from pydantic import BaseModel

from api.weather.models import Location


class ReportData(BaseModel):
    location: Location
    description: str


class Report(BaseModel):
    location: Location
    description: str
    created_at: datetime
