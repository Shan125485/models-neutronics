# TEMPLATE

from viz_neutronics.transport_correction import generate_mg_XS



# MC_output_file = "SimpleSlabVacuum_MC_output_1G.json"
# MC_output_file = "SimpleSlabVacuum_MC_output_23G.json"
MC_output_file = "SimpleSlabVacuum_MC_output_69G.json"
# MC_output_file = "SimpleSlabVacuum_MC_output_172G.json"

# tcType = 'outscatter'
tcType = 'flux limited'


generate_mg_XS(MC_output_file, tcType, switch='ON',plotting=True)
# generate_mg_XS(MC_output_file, tcType, switch='OFF')



# this will create a directory called materialsInputs with the materials XSfile inside.
