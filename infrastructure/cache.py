from datetime import datetime, timedelta
from settings import CACHE_LIFE_SEC


class Cacheble:
    def __init__(self) -> None:
        self.cache = {}

    def get(self, *args):
        key = "_".join(args)
        if not key in self.cache:
            return None
        delta:timedelta = (datetime.now() - self.cache[key]["created_at"])
        if delta.seconds > CACHE_LIFE_SEC:
            return None
        data = self.cache[key]["value"]
        print(f"GETTING FROM CACHE->{len(data)}chars")
        return data
    
    def set(self, *args, value=None):
        if not value:
            return None 
        key = "_".join(args)
        self.cache[key] = {
            "value":value,
            "created_at":datetime.now()
        }


GLOBAL_CACHE = Cacheble()