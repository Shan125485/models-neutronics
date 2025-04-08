# script
# from nuclearDataCalculator import results
import sys
print(sys.path)
from viz_neutronics.nuclearDensityCalculator import results
from nuclearDensityInputs import input



file_out = 'nuclearDensityOutputs.txt'


x = results(input)
x.display()
x.write_results(file_out)