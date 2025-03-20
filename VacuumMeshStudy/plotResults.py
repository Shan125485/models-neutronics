import numpy as np
# from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR, rmsError, plotFissionRatesCompareMC_RR, findFissRateMC, findFissRateRR

# inputFile = 'SimpleSlabVacuum_MC'
# outputFile = 'SimpleSlabVacuum_MC_output_23G.json'

# inputFile = 'SimpleSlabVacuum/SimpleSlabVacuum_MC'
outputFileMC = 'SimpleSlabVacuum_MC_output_69G.json'
# plotScatteringMatrices(outputFileMC)
# plotShannon(inputFile, outputFile)
# plotFissionRatesMC(outputFileMC, normalise=True)

# outputFileRR = 'SimpleSlabVacuum_RR_output.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_0.5.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_0.4.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_0.41.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_1.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_0.1.json'
# outputFileRR = 'SimpleSlabVacuum_RR_output_0.2.json'
outputFileRR = 'SimpleSlabVacuum_RR_output_0.333.json'


# plotFissionRatesRR(outputFileRR, normalise_plot=True, target=1)

rel_diff = plotFissionRatesCompareMC_RR(outputFileMC, outputFileRR, target=100)
# fissRateMC, fissMC_std = findFissRateMC(outputFileMC)
# fissRateRR, fissRR_std = findFissRateRR(outputFileRR)
# print(rmsError(actual_result=fissRateMC, predicted_result=fissRateRR))


