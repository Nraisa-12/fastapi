from fastapi import FastAPI

app = FastAPI()


icd10 = {
    "A00": "Cholera",
    "A01": "Typhoid fever",
    "A02": "Salmonella infections",
    # ...
}

cpt = {
    "10060": "Incision and drainage of abscess",
    "99213": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99214": "Office or other outpatient visit for the evaluation and management of an established patient",
    # ...
}

@app.get("/medical_codexes")
async def get_medical_codexes():
    return {"icd10": icd10, "cpt": cpt}














