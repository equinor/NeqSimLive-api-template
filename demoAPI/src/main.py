import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from neqsim.process import compressor, stream
from neqsim.thermo.thermoTools import fluid_df
from pydantic import BaseModel, Field


class compressorImpl(BaseModel):
    #Establish input parameters with defaualt values
    N2: float=0.01
    CO2: float=0.01
    methane: float=0.9
    ethane: float=0.1
    propane: float=0.03
    ibutane: float=.01
    nbutane: float=0.01
    npentane: float=0.001
    nhexane: float=0.001
    #Examples of documenting and setting range validation on input variables using Field type
    temperature_inlet: float = Field(20.0, title="Temperature of gas to compressor [°C]",lt=200.0, gt=-100.0, description="Temperature in range -100 to +200 °C")
    pressure_inlet: float = Field(25.0, title="Pressure of feed to compressor [bara]",lt=200.0, gt=0.0, description="Pressure in range 0 to 200 bara")
    temperature_outlet: float = Field(95.0, title="Temperature of discharge from compressor [°C]",lt=200.0, gt=-100.0, description="Temperature in range -100 to +200 °C")
    pressure_outlet: float = Field(60.0, title="Pressure of discharge from compressor [bara]",lt=1000.0, gt=0.0, description="Pressure in range 0 to 1000 bara")
    
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
    polytropicEfficiency: float = Field( title="Polytropic efficiency [-]",gt=0.0)
    polytropicFluidHead: float = Field( title="Polytropic fluid head [kJ/kg]",gt=0.0)


app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>NeqSim Live Demo API</title>
        </head>
        <body>
            <h1>NeqSim Live Demo API</h1>
            <a href="/docs">API documentation and testing</a><br>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

 
@app.post("/demoAPI/compressorCalc",response_model=compressorResults,description="Calculate the polytropic efficiency of a compressor")
def compressorCalc(compressor:compressorImpl):
    compresults = compressor.polytropicEfficiency()
    results = {
        'polytropicEfficiency': float(compresults[1]),
        'polytropicFluidHead': float(compresults[0])
    }
    return results
