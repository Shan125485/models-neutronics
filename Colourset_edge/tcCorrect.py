# TEMPLATE

from viz_neutronics.transport_correction import generate_mg_XS



# MC_output_file = "SimplePin_MC_output.json"
# resultsFile= 'Results/'

# filepathMC = 'FuelAssembly_MC_output.json'

filepathMC = 'Colourset_MC_output.json'



# tcType = 'outscatter'
tcType = 'flux limited'


generate_mg_XS(filepathMC, tcType, switch='ON', plotting=True)
# generate_mg_XS(filepathMC, tcType, switch='OFF', plotting=True)



# this will create a directory called materialsInputs with the materials XSfile inside.
