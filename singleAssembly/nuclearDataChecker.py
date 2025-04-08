# nuclear data density input

# calculate the nuclear density input


"""
Say we have material with chemical formula AxByCz

we can input the formula, and the overall density


"""


# Constants

L = 6.023e23 # avogadro's constant
b = 10**-24 # 1 barn in cm^2

def numberDensityCalculator(mass_density, input):
    Mr=0
    for data in input.values():
       
        Mr += data[0] * data[1]
    
    print('Mr:', Mr)
   
    area = L * mass_density * b / Mr
    print('Area', area)
    for key, value in input.items():
        print(key + ' : ' + str(value[1] * area))
    



# input atomic ratios

# 2% enriched UO2
input = {"U-235": (235,0.02), "U-238": (238, 0.98), "O": (8, 2)} 
mass_density = 10.97

# Gadolinium
input = {"Gd": (157,1)} 
mass_density = 7.9



numberDensityCalculator(mass_density, input)