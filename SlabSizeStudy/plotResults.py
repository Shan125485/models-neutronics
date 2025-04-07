#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR, plotFissionRatesCompareMC_RR

# inputFile = 'SimpleSlabVacuum_MC'
# outputFile = 'SimpleSlabVacuum_MC_output_23G.json'

# inputFile = 'SimpleSlabVacuum/SimpleSlabVacuum_MC'
outputFileMC = 'SimpleSlabVacuum_MC_output.json'
# plotScatteringMatrices(outputFile)




inputFile = 'SimpleSlabVacuum_RR'
# outputFile = 'SimpleSlabVacuum_RR_output_23G_fluxlimited.json'
# outputFile = 'SimpleSlabVacuum_RR_output_23G_reflective_test.json'
outputFileRR = 'SimpleSlabVacuum_RR_output.json'


plotShannon(inputFile, outputFileMC)
plotFissionRatesMC(outputFileMC, normalise_plot=True, target=100000)
plotFissionRatesRR(outputFileRR, normalise_plot=True)

plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR)


