from typing import Optional

import fastapi
from api.weather.models import Location
from services import wttr_in

weather_router = fastapi.APIRouter(prefix="/weather")


@weather_router.get("/")
async def weather(loc: Location = fastapi.Depends(), units: Optional[str] = None):
    report = await wttr_in.async_get_report_png(loc.city, units)
    body = f"<a href='/'>Back to main page</a><hr><pre>{report}</pre>"
    return fastapi.responses.HTMLResponse(content=body)
