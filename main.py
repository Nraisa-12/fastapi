from fastapi import FastAPI

app = FastAPI()

codexes = {
    "ICD-10": ["A00", "A01", "B00", "B01"],
    "CPT": ["10021", "10022", "10040", "10060"]
}

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/codex/{codex_name}")
def read_codex(codex_name: str):
    if codex_name not in codexes:
        return {"Error": "Codex not found"}
    return {"Codex": codex_name, "Codes": codexes[codex_name]}







