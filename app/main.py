from fastapi import FastAPI

app = FastAPI(
    title="payment orchestration",
    version="0.1.0"
)

@app.get("/health-check")
def health_check(): 
    return {"status" : "ok"}