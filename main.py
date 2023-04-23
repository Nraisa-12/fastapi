from fastapi import FastAPI

app = FastAPI()

med_codex1 = ["code1", "code2", "code3"]
med_codex2 = ["codeA", "codeB", "codeC"]

@app.get("/med_codexes")
async def get_med_codexes():
    return {"med_codex1": med_codex1, "med_codex2": med_codex2}










