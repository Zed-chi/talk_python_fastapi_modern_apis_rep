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
    body = """
    <h1>Hello, this is a dump page</h1>
    <a href='/api/calculate'>Test route with empty params</a>
    <hr>
    <a href='/api/calculate?x=1&y=2&z=3'>Test route with 1, 2, 3</a>
    <hr>
    <a href='/api/calculate?x=1&y=2'>Test route with 1, 2</a>
    <hr>
    """
    return fastapi.responses.HTMLResponse(content=body) 


if __name__ == "__main__":
    uvicorn.run(api)
