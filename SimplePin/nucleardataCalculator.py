from viz_neutronics.nuclearDensityCalculator import results
from viz_neutronics.nuclearDensityInputs import UO2, H2O



file_out = 'nuclearDensityOutputs.txt'


# input = {"UO2": UO2  } 
input = {"H2O": H2O  } 

x = results(input)
x.display()
x.write_results(file_out)