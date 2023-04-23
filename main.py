from fastapi import FastAPI

app = FastAPI()

medical_codexes = {
    "icd-10": {
        "description": "International Classification of Diseases, 10th Revision",
        "url": "https://www.who.int/classifications/icd/icdonlineversions/en/"
    },
    "cpt": {
        "description": "Current Procedural Terminology",
        "url": "https://www.ama-assn.org/practice-management/cpt"
    }
}

@app.get("/")
async def root():
    return {"message": "Welcome to the medical codex API."}

@app.get("/codexes/")
async def get_codexes():
    return medical_codexes

@app.get("/codexes/{codex_name}")
async def get_codex(codex_name: str):
    if codex_name not in medical_codexes:
        return {"error": "Invalid medical codex."}
    return medical_codexes[codex_name]












