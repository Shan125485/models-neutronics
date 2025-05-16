#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotSpatialTallyMC, plotSpatialTallyRR, plotFissionRatesCompareMC_RR, plotFissionRatesRR, plotSpatialTallyCompare_MCRR, plotSpatialTallyCompare_MCMG, plotSpatialMaterialTallyMC

inputFileMC = 'quarterCore_MC'
# outputFileMC = 'output.json'
outputFileMC = 'quarterCore_MC_output.json'
# outputFileMCMG = 'Colourset_MCMG_output.json'


# inputFileRR = 'quarterCore_RR'
outputFileRR = 'quarterCore_RR_output.json'

tallyName_MC = 'pinFiss'
tallyName_MC_assem = 'assemblyFissRadial'

# tallyName_MCMG = 'pinFiss'
tallyName_RR = 'fiss1G'

tallyName_RR2 = 'flux1G'


# RR visualisation

# plotSpatialTallyMC(outputFileMC, tallyName_MC, normalise_by_mean='non-zero', response_index=0, visualise_quarter='bottom-right')
# plotSpatialTallyMC(outputFileMC, tallyName_MC_assem, normalise_by_mean='non-zero', response_index=0, visualise_quarter='bottom-right')

plotSpatialTallyMC(outputFileMC, tallyName_MC, normalise_by_mean='non-zero', response_index=0, visualise_quarter=False)
plotSpatialTallyMC(outputFileMC, tallyName_MC_assem, normalise_by_mean='non-zero', response_index=0, visualise_quarter=False)
plotSpatialTallyMC(outputFileMC, tallyName_MC, normalise_by_mean='non-zero', response_index=1, visualise_quarter=False)
plotSpatialTallyMC(outputFileMC, tallyName_MC_assem, normalise_by_mean='non-zero', response_index=1, visualise_quarter=False)



# plotSpatialMaterialTallyMC(outputFileMC,'u238Capture', materialName='UO2-16' ,normalise_by_mean='all', response_index=0)
# plotSpatialMaterialTallyMC(outputFileMC,'u238Capture', materialName='UO2-31' ,normalise_by_mean='all', response_index=0)

# plotSpatialTallyRR(outputFileRR,tallyName_RR, normalise_by_mean='non-zero', visualise_quarter=False)
# plotSpatialTallyRR(outputFileRR,tallyName_RR2, normalise_by_mean='non-zero', visualise_quarter=False)
# plotSpatialTallyCompare_MCRR(outputFileMC, outputFileRR, tallyName_MC, tallyName_RR2, normalise_by_mean='non-zero', response_index_MC=0, visualise_quarter=False)
# # plotSpatialTallyCompare_MCRR(outputFileMC, outputFileRR, tallyName_MC, tallyName_RR, normalise_by_mean='non-zero', response_index_MC=1, visualise_quarter=False)
# plotSpatialTallyCompare_MCMG(outputFileMC,outputFileMCMG, tallyName_MC, tallyName_MCMG, normalise_by_mean='all', response_index_CE=0, response_index_MG=0, visualise_quarter=False)


