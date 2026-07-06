from fastapi import FastAPI

app = FastAPI(title="GeoGuardAI API")

@app.get("/")
def root():
    return {"message": "GeoGuardAI Backend Running 🚀"}