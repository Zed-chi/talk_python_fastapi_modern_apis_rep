from typing import Optional

import fastapi
import uvicorn
import json

api = fastapi.FastAPI()

@api.get("/api/calculate")
def calculate(x:int=1, y:int=1, z:Optional[int]=None):
    res = x+y
    if z:
        res+=z
    return fastapi.Response(
        content=json.dumps({"value": res}),
        status_code=200 
    ) 



@api.get("/")
def index():
    return "<a>qwe</a>"


if __name__ == "__main__":
    uvicorn.run(api)
