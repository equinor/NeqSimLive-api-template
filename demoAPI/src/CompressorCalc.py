import pandas as pd
from neqsim.process import compressor, stream
from neqsim.thermo.thermoTools import fluid_df
from pydantic import BaseModel


class CompressorCalc(BaseModel):
    N2: float = 0.01
    CO2: float = 0.01
    methane: float = 0.9
    ethane: float = 0.1
    propane: float = 0.03
    ibutane: float = .01
    nbutane: float = 0.01
    npentane: float = 0.001
    nhexane: float = 0.001

    temperature_inlet: float = 20.0
    pressure_inlet: float = 25.0
    temperature_outlet: float = 95.0
    pressure_outlet: float = 60.0

    def polytropicEfficiency(self):
        gascondensate = {
            'ComponentName':  ["nitrogen", "CO2", "methane", "ethane", "propane", "i-butane", "n-butane", "n-pentane", "n-hexane"],
            'MolarComposition[-]':  [self.N2, self.CO2, self.methane, self.ethane, self.propane, self.ibutane, self.nbutane, self.npentane, self.nhexane],
        }
        gascondensateFluid = fluid_df(pd.DataFrame(
            gascondensate), lastIsPlusFraction=False)
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


class CompressorResult(BaseModel):
    polytropicEfficiency: float
    polytropiFluidHeaad: float
