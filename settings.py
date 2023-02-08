from environs import Env
from starlette.templating import Jinja2Templates

env = Env()
env.read_env()


HTML_DIR = env.str("HTML_DIR", "templates")
ASSETS_DIR = env.str("ASSETS_DIR")
GLOBAL_CACHE = {}
CACHE_LIFE_SEC = env.int("CACHE_LIFE_SEC", 180)
DB = []
template_manager = Jinja2Templates(HTML_DIR)
