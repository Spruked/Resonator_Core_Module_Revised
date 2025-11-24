from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from resonator import Resonator

app = FastAPI(title="Resonator API")
resonator = Resonator()

class InputData(BaseModel):
    input: dict
    telemetry: bool = True

@app.post("/resonate")
def resonate(data: InputData):
    return resonator.process(data.input, telemetry=data.telemetry)

@app.get("/")
def root():
    return {"status": "Resonator API running"}

@app.get("/handshake")
def handshake():
    return {"status": "handshake_success", "module": "Resonator"}

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    html = f"""
    <html>
    <head><title>Resonator Dashboard</title></head>
    <body>
    <h1>Resonator Dashboard</h1>
    <p>Requests: {resonator.request_count}</p>
    <p>Errors: {resonator.error_count}</p>
    </body>
    </html>
    """
    return html

@app.get("/metrics")
def metrics():
    return {"requests": resonator.request_count, "errors": resonator.error_count}
