from fastapi import FastAPI

app = FastAPI()

medical_codex1 = {"code": "ABC123", "name": "Medical Codex 1"}
medical_codex2 = {"code": "DEF456", "name": "Medical Codex 2"}

@app.get("/")
async def root():
    return {"Medical Codex API"}

@app.get("/codex1")
async def get_codex1():
    return medical_codex1

@app.get("/codex2")
async def get_codex2():
    return medical_codex2













