#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotSpatialTallyMC, plotSpatialTallyRR, plotFissionRatesCompareMC_RR, plotFissionRatesRR, plotSpatialTallyCompare_MCRR, plotSpatialTallyCompare_MCMG

inputFileMC = 'QuarterAssembly_MC'
outputFileMC = 'QuarterAssembly_MC_output.json'
outputFileMCMG = 'QuarterAssembly_MC_MG_output.json'


inputFileRR = 'QuarterAssembly_RR'
outputFileRR = 'QuarterAssembly_RR_output.json'

tallyName_MC = 'pinFiss'
tallyName_MCMG = 'pinFiss'
tallyName_RR = 'fiss1G'


# RR visualisation
plotSpatialTallyRR(outputFileRR,tallyName_RR, visualise_quarter=True)
plotSpatialTallyMC(outputFileMC, tallyName_MC, normalise_by_mean='all', visualise_quarter=True)
plotSpatialTallyCompare_MCRR(outputFileMC, outputFileRR, tallyName_MC, tallyName_RR, normalise_by_mean='all', response_index_MC=0, visualise_quarter=True)
# plotSpatialTallyCompare_MCMG(outputFileMC,outputFileMCMG, tallyName_MC, tallyName_MCMG, normalise_by_mean='all', response_index_CE=0, response_index_MG=0, visualise_quarter=True)


# plotSpatialTallyRR(outputFileRR,'flux1G') # should be plot Energy Tally TODO
# TODO add a reaction rates tallying option to random ray?
# plotFissionRatesRR(outputFileRR, target=100)
# plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR,target = 100)



