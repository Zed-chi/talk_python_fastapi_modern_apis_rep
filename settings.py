from environs import Env


env = Env()
env.read_env()


HTML_DIR = env.str("HTML_DIR", "templates")
ASSETS_DIR = env.str("ASSETS_DIR")
GLOBAL_CACHE = {}
CACHE_LIFE_SEC = env.int("CACHE_LIFE_SEC", 180)