# TEMPLATE

from viz_neutronics.transport_correction import generate_mg_XS



# resultsFile= 'Results/'

# filepathMC = 'FuelAssembly_MC_output.json'

# filepathMC = 'Colourset_MC_output.json'

# filepathMC = 'outputs_aniso_ref_flux_limited/Colourset_MC_output_2G.json'
# filepathMC = 'outputs_aniso_ref_flux_limited/Colourset_MC_output_8G.json'
filepathMC = 'outputs_aniso_ref_flux_limited/Colourset_MC_output_70G.json'


tcType = 'outscatter'
# tcType = 'flux limited'


generate_mg_XS(filepathMC, tcType, switch='ON', plotting=True)
# generate_mg_XS(filepathMC, tcType, switch='OFF', plotting=True)



# this will create a directory called materialsInputs with the materials XSfile inside.
