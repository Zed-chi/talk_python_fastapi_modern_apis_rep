import fastapi
import uvicorn
from environs import Env
from fastapi.staticfiles import StaticFiles

from api.router import api_router
from services.report_service import get_hour_report
from settings import ASSETS_DIR, template_manager

env = Env()
env.read_env()


api = fastapi.FastAPI()
api.mount("/static", StaticFiles(directory=ASSETS_DIR), name="static")
api.include_router(api_router)


@api.get("/", name="index")
def index(request: fastapi.Request):
    report = get_hour_report()
    return template_manager.TemplateResponse(
        "./index.html", context={"request": request, "report": report}
    )


@api.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/icon.ico")


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")
