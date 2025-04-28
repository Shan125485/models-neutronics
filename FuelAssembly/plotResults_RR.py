#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotSpatialTallyRR, plotFissionRatesCompareMC_RR, plotFissionRatesRR, plotSpatialTallyCompare

# inputFileMC = 'FuelAssembly_MC'
# outputFileMC = 'FuelAssembly_MC_output.json'


inputFileMC = 'QuarterAssembly_MC'
outputFileMC = 'QuarterAssembly_MC_output.json'


# inputFileRR = 'FuelAssembly_RR'
# outputFileRR = 'FuelAssembly_RR_output.json'
inputFileRR = 'QuarterAssembly_RR'
outputFileRR = 'QuarterAssembly_RR_output.json'


tallyName_MC = 'pinFiss'
tallyName_RR = 'fiss1G'


# RR visualisation
# plotSpatialTallyRR(outputFileRR,'fiss1G', visualise_quarter=True)
plotSpatialTallyCompare(outputFileMC, outputFileRR, tallyName_MC, tallyName_RR, normalise_by_mean='all', response_index_MC=0, visualise_quarter=True)


# plotSpatialTallyRR(outputFileRR,'flux1G') # should be plot Energy Tally TODO
# TODO add a reaction rates tallying option to random ray?
# plotFissionRatesRR(outputFileRR, target=100)
# plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR,target = 100)



