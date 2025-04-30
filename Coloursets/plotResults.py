#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotSpatialTallyMC, plotSpatialTallyRR, plotFissionRatesCompareMC_RR, plotFissionRatesRR, plotSpatialTallyCompare_MCRR, plotSpatialTallyCompare_MCMG, plotSpatialMaterialTallyMC

inputFileMC = 'Coloursets_MC'
outputFileMC = 'Coloursets_MC_output.json'
outputFileMCMG = 'Coloursets_MC_MG_output.json'


inputFileRR = 'Coloursets_RR'
outputFileRR = 'Coloursets_RR_output.json'

tallyName_MC = 'pinFiss'
tallyName_MCMG = 'pinFiss'
tallyName_RR = 'fiss1G'


# RR visualisation

plotSpatialTallyMC(outputFileMC, tallyName_MC, normalise_by_mean='non-zero', visualise_quarter=False)
plotSpatialMaterialTallyMC(outputFileMC,'u238Capture', materialName='UO2-16' ,normalise_by_mean='all', response_index=0)
plotSpatialMaterialTallyMC(outputFileMC,'u238Capture', materialName='UO2-31' ,normalise_by_mean='all', response_index=0)

# plotSpatialTallyRR(outputFileRR,tallyName_RR, visualise_quarter=False)
# plotSpatialTallyCompare_MCRR(outputFileMC, outputFileRR, tallyName_MC, tallyName_RR, normalise_by_mean='all', response_index_MC=0, visualise_quarter=False)
# plotSpatialTallyCompare_MCMG(outputFileMC,outputFileMCMG, tallyName_MC, tallyName_MCMG, normalise_by_mean='all', response_index_CE=0, response_index_MG=0, visualise_quarter=False)


