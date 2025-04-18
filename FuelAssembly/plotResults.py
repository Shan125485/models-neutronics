#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotShannon, plotScatteringMatrices,  plotFluxMC, plotFissionRatesMC, plotFluxSpectrumMC, plotFissionRatesRR, plotFissionRatesCompareMC_RR

inputFileMC = 'FuelAssembly_MC'
outputFileMC = 'FuelAssembly_MC_output.json'


inputFileRR = 'SimplePin_RR'
outputFileRR = 'SimplePin_RR_output.json'


# MC visualisation
plotShannon(inputFileMC, outputFileMC)

# plotFluxMC(outputFileMC, target=100)
plotFissionRatesMC(outputFileMC, target=100)

# RR visualisation
# plotFissionRatesRR(outputFileRR, target=100)
# plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR,target = 100)

# plotFluxSpectrumMC(outputFileMC)


