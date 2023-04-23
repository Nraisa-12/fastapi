from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Medical codex"}

@app.get("/medical-codex-1")
async def read_medical_codex_1():
    return {"code": "A01.0", "description": "Typhoid fever"}

@app.get("/medical-codex-2")
async def read_medical_codex_2():
    return {"code": "C50.9", "description": "Breast cancer, unspecified"}

