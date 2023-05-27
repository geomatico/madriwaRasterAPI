from fastapi import FastAPI

API_VERSION = "v1"

app = FastAPI()


@app.post(f"/api/{API_VERSION}/isladecalor/lts")
async def heat_inland():
    return {"message": "Hello World"}
