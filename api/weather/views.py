from typing import Optional

import fastapi

from api.weather.models import Location
from services import wttr_in

weather_router = fastapi.APIRouter(prefix="/weather")


@weather_router.get("/")
def weather(loc: Location = fastapi.Depends(), units: Optional[str] = None):
    report = wttr_in.get_report_png(loc.city, units)
    body = f"<pre>{report}</pre>"
    return fastapi.responses.HTMLResponse(content=body)
