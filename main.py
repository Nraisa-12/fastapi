from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_icd_codes():
    icd1 = {
        "code": "A01.1",
        "description": "Typhoid fever"
    }
    icd2 = {
        "code": "B25.9",
        "description": "Cytomegaloviral disease, unspecified"
    }
    return {"icd1": icd1, "icd2": icd2}















