from fastapi import FastAPI

app = FastAPI()

med_codex1 = ["code1", "code2", "code3"]
med_codex2 = ["code4", "code5", "code6"]

@app.get("/")
async def root():
    return {"message": "Welcome to the medical codex API!"}

@app.get("/codex1")
async def get_codex1():
    return {"codex1": med_codex1}

@app.get("/codex2")
async def get_codex2():
    return {"codex2": med_codex2}





