import fastapi


weather_router = fastapi.APIRouter(prefix="/weather")

@weather_router.get("")
def weather(city, units):
    return fastapi.responses.RedirectResponse(url="/static/icon.ico")
