from fastapi import FastAPI

app = FastAPI()

icd_10 = {
    "A00": "Cholera",
    "A01": "Typhoid fever",
    "B02": "Varicella",
}

icd_11 = {
    "BA00": "Cholera",
    "BA01": "Typhoid fever",
    "BB02": "Varicella",
}

@app.get("/icd-10")
async def get_icd_10():
    return icd_10

@app.get("/icd-11")
async def get_icd_11():
    return icd_11




