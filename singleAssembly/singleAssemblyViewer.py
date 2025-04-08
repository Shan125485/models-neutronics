import json
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches

from input2json import parse_text_to_dict, save_to_json, stringTuple_to_array, dict2obj


# returns output JSON object as python dictionary
with open('output.json') as f:
    outputDict = json.load(f)

output = dict2obj(outputDict)
fissionResults = np.array(output.active.pinFiss.Res).T
x_coords = np.array(output.active.pinFiss.XBounds).T
y_coords = np.array(output.active.pinFiss.YBounds).T
print(x_coords)
print(y_coords)
print(fissionResults.shape)
print(fissionResults)

x_coords_averaged =  (x_coords[0,:] + x_coords[1,:]) / 2
y_coords_averaged =  (y_coords[0,:] + y_coords[1,:]) / 2

fissionResults_std = fissionResults[1,0].T
print('std')
print(fissionResults_std)
fissionResults_values = fissionResults[0,0].T

# xx, yy = np.meshgrid(x_coords_averaged, y_coords_averaged)



"""
im = plot.imshow(x_coords_averaged, y_coords_averaged, fissionResults_values)

# get the colors of the values, according to the 
# colormap used by imshow
values = np.unique(fissionResults_values.ravel())
colors = [ im.cmap(im.norm(value)) for value in values]
# create a patch (proxy artist) for every color 
patches = [ mpatches.Patch(color=colors[i], label="Level {:.2f}".format(values[i]) ) for i in range(len(values)) ]
# put those patched as legend-handles into the legend
plot.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )
"""
#%% 
#plot.show()
#%%
# plot.contourf(fissionResults_values)

fig, (ax1, ax2) = plot.subplots(1,2, sharex='col', sharey=True)
# val = ax1.pcolormesh( x_coords_averaged, y_coords_averaged, fissionResults_values)
val = ax1.contourf( x_coords_averaged, y_coords_averaged, fissionResults_values)
val2 = ax2.imshow( fissionResults_values)
# val2 = ax2.tricontourf(xx, yy, fissionResults_values)

ax1.set_title('pcolormesh')
ax2.set_title('contourf')

# ax3.set_title('imshow')
fig.colorbar(val)
fig.suptitle("Nx=2, Ny=3")
# plot.gca().set_aspect('equal', adjustable=None)
plot.tight_layout()
plot.savefig('fissionpin.png')




# # view k_eff
# keff = outputDict.get("keff")
# active = outputDict.get("active")
# pinFiss = active.get("pinFiss")
# pinfiss


inputDict = parse_text_to_dict('singleAssembly')
save_to_json(inputDict, 'input.json')
input = dict2obj(inputDict)

# # print(inputDict)


# # get values from input
# geometry = inputDict.get('geometry')
# surface = geometry.get('surfaces').get('squareBound')
# origin = surface.get('origin')
# halfwidth = surface.get('halfwidth')
# halfwidth = stringTuple_to_array(halfwidth)


# get values from output
# cycles   = dictionary.get('Inactive_Cycles')
# inactive = dictionary.get('inactive')
# shannon  = inactive.get('shannon')
# results  = shannon.get('shannonEntropy')
# results_mean = np.array(results[1:cycles])


# activeTally = dictionary.get('active')
# totalPower = activeTally.get('totalPow').get('Res')

# plot results
# fig, ax = plt.subplots()
# ax.plot(results_mean)
# ax.set_xlabel("Inactive cycle number [-]")
# ax.set_ylabel("Shannon Entropy [-]")
# # ax.set_title('{:.0f} inactive cycles. Dimensions of bounding surface: {:.1f} x {:.1f} x {:.1f} cm'.format(cycles, 2*halfwidth[0], 2*halfwidth[1], 2*halfwidth[2]))

# plt.savefig('shannon.png')
# plt.show()