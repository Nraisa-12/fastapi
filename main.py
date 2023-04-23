from fastapi import FastAPI

app = FastAPI()

@app.get("/icd10")
def get_icd10():
    return {"icd10": ["A00", "A01", "A02", ... ]}

@app.get("/cpt")
def get_cpt():
    return {"cpt": ["10021", "10022", "10030", ... ]}



