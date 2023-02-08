import fastapi

from api.reports.views import reports_router
from api.weather.views import weather_router

api_router = fastapi.APIRouter(prefix="/api")
api_router.include_router(weather_router)
api_router.include_router(reports_router)
