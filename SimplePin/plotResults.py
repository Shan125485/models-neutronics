#from plottingFunctions import plotShannon, plotScatteringMatrices, plotFissionRatesMC, readInputs, readOutputs, plotFissionRatesRR
from viz_neutronics.plottingFunctions import  plotShannon, plotScatteringMatrices, plotFissionRatesMC_radial, plotFluxMC, plotFissionRatesRR_radial, plotFissionRatesCompare_radial_MC_RR

inputFileMC = 'SimplePin_MC'
outputFileMC = 'SimplePin_MC_output.json'


inputFileRR = 'SimplePin_RR'
outputFileRR = 'SimplePin_RR_output.json'


# plotScatteringMatrices(outputFileMC)
# plotShannon(inputFileMC, outputFileMC)
plotFissionRatesMC_radial(outputFileMC, normalise_plot=True, target=100)
# plotFluxMC(outputFileMC, target=100)
plotFissionRatesRR_radial(outputFileRR, normalise_plot=True, target=100)

plotFissionRatesCompare_radial_MC_RR(outputFileMC, outputFileRR)


