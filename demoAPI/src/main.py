from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from CompressorCalc import CompressorCalc, CompressorResult

app = FastAPI()


@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>NeqSim Live Demo API</title>
        </head>        <body>
            <h1>NeqSim Live Demo API</h1>
            <a href="/docs">API documentation and testing</a><br>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/compressorCalc", response_model=CompressorResult, description="Calculate the polytropic efficiency of a compressor")
def compressor_calc(compressor: CompressorCalc):
    compresults = compressor.polytropicEfficiency()
    results = {
        'polytropicEfficiency': float(compresults[1]),
        'polytropiFluidHeaad': float(compresults[0])
    }
    return results
