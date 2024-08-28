from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"Hello Pak Army"}
@app.get('/pak')
def read_root():
    return {"message":"Hello Pak Army and all pakistan"}

@app.get('/ind')
def aaa():
    return {"message":"india army"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port="8000")