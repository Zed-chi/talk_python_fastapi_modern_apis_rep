import fastapi

from api.weather import views

api_router = fastapi.APIRouter(prefix="/api")
api_router.include_router(views.weather_router)
