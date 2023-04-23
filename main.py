from fastapi import FastAPI

app = FastAPI()

codexes = {
    "icd10": [
        {"code": "A00", "description": "Cholera"},
        {"code": "B10", "description": "Viral hepatitis"},
        {"code": "C15", "description": "Malignant neoplasm of oesophagus"},
    ],
    "cpt": [
        {"code": "10021", "description": "Fine needle aspiration; without imaging guidance"},
        {"code": "99213", "description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: a problem focused history; a problem focused examination; straightforward medical decision making."},
        {"code": "96372", "description": "Therapeutic, prophylactic, or diagnostic injection (specify substance or drug); subcutaneous or intramuscular"},
    ],
}

@app.get("/")
async def root():
    return {"message": "Medical codex API."}

@app.get("/codexes")
async def get_codexes():
    return codexes

@app.get("/codexes/{codex}")
async def get_codex(codex: str):
    if codex not in codexes:
        return {"error": f"Invalid codex '{codex}'. Allowed codexes are {', '.join(codexes.keys())}."}
    return codexes[codex]











