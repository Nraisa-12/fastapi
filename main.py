from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the medical codexes API!"}

@app.get("/codex1")
def read_codex1():
    codex1 = {
        "ICD-10": "International Classification of Diseases, 10th Revision",
        "CPT": "Current Procedural Terminology",
        "HCPCS": "Healthcare Common Procedure Coding System"
    }
    return codex1

@app.get("/codex2")
def read_codex2():
    codex2 = {
        "SNOMED CT": "Systematized Nomenclature of Medicine Clinical Terms",
        "LOINC": "Logical Observation Identifiers Names and Codes",
        "RxNorm": "United States National Library of Medicine's standard clinical drug vocabulary"
    }
    return codex2








