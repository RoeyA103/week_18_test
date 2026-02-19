from fastapi import FastAPI
from routes import route
from time import sleep
import uvicorn


app = FastAPI()

app.include_router(route)

@app.get("/")
def root():
    return {"message":"healthy"}


if __name__=="__main__":
    uvicorn.run("main:app",host="localhost",port=8080,reload=True)