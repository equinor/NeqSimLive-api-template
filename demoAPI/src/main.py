from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from neqsim.thermo.thermoTools import fluid_df
from neqsim.process import stream,  compressor
import pandas as pd

class compressorCalc(BaseModel):
    N2: float=0.01
    CO2: float=0.01
    methane: float=0.9
    ethane: float=0.1
    propane: float=0.03
    ibutane: float=.01
    nbutane: float=0.01
    npentane: float=0.001
    nhexane: float=0.001
   
    temperature_inlet: float = 20.0
    pressure_inlet: float = 25.0
    temperature_outlet: float = 95.0
    pressure_outlet: float = 60.0
    
    def polytropicEfficiency(self):
        gascondensate = {
            'ComponentName':  ["nitrogen", "CO2", "methane", "ethane", "propane", "i-butane", "n-butane", "n-pentane", "n-hexane"], 
            'MolarComposition[-]':  [self.N2, self.CO2, self.methane, self.ethane, self.propane, self.ibutane, self.nbutane, self.npentane, self.nhexane], 
          }
        gascondensateFluid = fluid_df(pd.DataFrame(gascondensate), lastIsPlusFraction=False)
        gascondensateFluid.setPressure(self.pressure_inlet, "bara")
        gascondensateFluid.setTemperature(self.temperature_inlet, "C")
        inStream = stream(gascondensateFluid)
        compressor1 = compressor(inStream)
        compressor1.setOutletPressure(self.pressure_outlet, 'bara')
        compressor1.setOutTemperature(self.temperature_outlet+273.15)
        compressor1.setUsePolytropicCalc(True)
        inStream.run()
        compressor1.run()
        return [compressor1.getPolytropicFluidHead(), compressor1.getPolytropicEfficiency()]

class compressorResults(BaseModel):
    polytropicEfficiency: float
    polytropiFluidHeaad: float


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

 
@app.post("/compressorCalc",response_model=compressorResults,description="Calculate the polytropic efficiency of a compressor")
def compressorCalc(compressor:compressorCalc):
    compresults = compressor.polytropicEfficiency()
    results = {
        'polytropicEfficiency': float(compresults[1]),
        'polytropiFluidHeaad': float(compresults[0])
    }
    return results