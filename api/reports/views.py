import fastapi

from api.weather.models import Location
from services import report_service
from settings import template_manager

reports_router = fastapi.APIRouter(prefix="/reports")


@reports_router.get("/")
async def get_reports(request: fastapi.Request):
    reports = report_service.get_hour_report()
    return template_manager.TemplateResponse(
        "./reports/add_report.html",
        context={"request": request, "reports": reports},
    )


@reports_router.post("/add")
async def add_report_view(
    city: str = fastapi.Form(), description: str = fastapi.Form()
):
    print(f"=== {city} ====")
    location = Location(city=city)
    report_service.add_report(location, description)
    return fastapi.responses.RedirectResponse("/", status_code=301)
