#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotShannon, plotSpatialTallyMC, plotSpatialMaterialTallyMC, plotFluxSpectrumMC, plotFissionRatesRR, plotFissionRatesCompareMC_RR

inputFileMC = 'FuelAssembly_MC'
outputFileMC = 'FuelAssembly_MC_output.json'

inputFileMC = 'QuarterAssembly_MC'
outputFileMC = 'QuarterAssembly_MC_output.json'


# MC visualisation
plotShannon(inputFileMC, outputFileMC)

# plotFluxMC(outputFileMC, target=100)
# plotSpatialTallyMC(outputFileMC, tallyName='pinFiss', normalise_by_mean='all')
plotSpatialTallyMC(outputFileMC, tallyName='pinFiss', normalise_by_mean='all', visualise_quarter=True)
# plotSpatialTallyMC(outputFileMC, tallyName='u238Capture', normalise_by_mean='all')
# plotSpatialMaterialTallyMC(outputFileMC, tallyName='u238Capture', materialName='UO2-31', normalise_by_mean='all')

# plotFissionRatesMC(outputFileMC, target=100)

# RR visualisation
# plotFissionRatesRR(outputFileRR, target=100)
# plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR,target = 100)

# plotFluxSpectrumMC(outputFileMC)


