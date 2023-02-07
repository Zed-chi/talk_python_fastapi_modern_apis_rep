import fastapi
import uvicorn
from environs import Env
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from api.router import api_router

env = Env()
env.read_env()


api = fastapi.FastAPI()
template_manager = Jinja2Templates(env.str("HTML_DIR", "templates"))
api.mount(
    "/static", StaticFiles(directory=env.str("ASSETS_DIR")), name="static"
)
api.include_router(api_router)


@api.get("/")
def index(request: fastapi.Request):
    return template_manager.TemplateResponse(
        "./index.html", context={"request": request}
    )


@api.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/icon.ico")


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")
