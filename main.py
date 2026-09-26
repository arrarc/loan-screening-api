from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

VERSION = "v1"

class LoanRequest(BaseModel):
    name: str
    income: int
    loan_amount: int

@app.get("/")
def root():
    return {"service": "住宅ローン事前審査API", "version": VERSION}

@app.post("/screening")
def screening(req: LoanRequest):
    ratio = req.loan_amount / req.income
    if ratio <= 5:
        result = "仮審査通過"
    elif ratio <= 8:
        result = "要審査"
    else:
        result = "仮審査否決"
    return {
        "name": req.name,
        "income": req.income,
        "loan_amount": req.loan_amount,
        "ratio": round(ratio, 2),
        "result": result,
        "version": VERSION
    }
