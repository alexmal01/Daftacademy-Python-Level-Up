from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root_view():
    return {"message" : "Hello world!"}

@app.get("/method/{name}")
async def method_name_view(name: str):
    return {"method" : name}