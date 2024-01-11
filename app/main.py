import uvicorn
from fastapi import FastAPI

from app.endpoints import dish_endpoint, tag_endpoint, category_endpoint, photo_endpoint

app = FastAPI(prefix="/api")
app.include_router(dish_endpoint.router, tags=['dish'])
app.include_router(tag_endpoint.router, tags=['tag'])
app.include_router(category_endpoint.router, tags=['category'])
app.include_router(photo_endpoint.router, tags=['photo'])

'''
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=1337,
        reload=False
    )
'''