from fastapi import FastAPI

app = FastAPI()


icd10 = {
    "A00": "Cholera",
    "B37": "Candidiasis",
    "C50": "Malignant neoplasm of breast"
}

cpt = {
    "10021": "Fine needle aspiration; without imaging guidance",
    "99213": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: an expanded problem focused history, an expanded problem focused examination, medical decision making of low complexity."
}


@app.get("/icd10")
async def get_icd10():
    return icd10

@app.get("/cpt")
async def get_cpt():
    return cpt









