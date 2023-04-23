from fastapi import FastAPI

app = FastAPI()

# define two different medical codexes
icd_codes = [
    {"code": "A00", "description": "Cholera"},
    {"code": "A01", "description": "Typhoid and paratyphoid fevers"},
    {"code": "A02", "description": "Other salmonella infections"},
]

cpt_codes = [
    {"code": "10021", "description": "Fine needle aspiration; without imaging guidance"},
    {"code": "10022", "description": "Fine needle aspiration; with imaging guidance"},
    {"code": "10030", "description": "Guidance for insertion of needle into muscle for electromyography"},
]

@app.get("/icd_codes")
async def get_icd_codes():
    return icd_codes

@app.get("/cpt_codes")
async def get_cpt_codes():
    return cpt_codes


