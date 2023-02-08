from datetime import datetime

from api.reports.models import Report
from api.weather.models import Location
from settings import DB


def get_hour_report() -> list:
    now = datetime.now()
    hour_reports = list(
        filter(lambda el: (now - el.created_at).seconds < 3600, DB)
    )
    DB.clear()
    DB.extend(hour_reports)
    return sorted(hour_reports, key=lambda x: x.created_at)


def add_report(location: Location, description: str):
    report = Report(
        location=location, description=description, created_at=datetime.now()
    )
    DB.append(report)
