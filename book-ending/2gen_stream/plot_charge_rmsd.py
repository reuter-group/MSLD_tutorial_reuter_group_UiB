import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

dim1 = 2
dim2 = 6
total_plots = dim1*dim2
fig, axs = plt.subplots(dim1, dim2)
fig.set_size_inches(20, 10)
fig.dpi = 200

nsubs=10
combs = [(2,2), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (3, 9)]


# Make a plot for each ligand
for mol,ax in enumerate(axs.reshape(-1)):
    molid = mol + 1
    try:
        sub1 = combs[mol][0]
        sub2 = combs[mol][1]
    except IndexError:
        break
    if os.path.isfile(f's1s{sub1}.s2s{sub2}_crn2ff_qpert.str' ):   
       # Retrieve charge sets
       ff_str = np.genfromtxt(f's1s{sub1}.s2s{sub2}_crn2ff_qpert.str' , dtype=str, skip_header=3, skip_footer=2)
       ff = np.array(ff_str[:, 3], dtype=float)
       crn_str = np.genfromtxt(f's1s{sub1}.s2s{sub2}_ff2crn_qpert.str', dtype=str, skip_header=3, skip_footer=2)
       crn =  np.array(crn_str[:, 3], dtype=float)

       # Paste the two columns side by side
       ff_crn = np.column_stack((ff, crn))

       # Calculate the RMSD
       rmsd = np.sqrt(np.mean((crn - ff) ** 2))

       # Plot them
       ax.scatter(ff,crn,marker='o',linewidth=0.5)
    
       # Plot y=x line
       ax.axline((0, 0), slope=1)
    
       # Axis specs:
       ## Title
       ax.set_title(f's1s{sub1}.s2s{sub2} - QRMSD={rmsd:.4f}',fontsize=5)
    
    ## Scale
    #ax.set_xlim(-0.9,0.7)
    #ax.set_ylim(-0.9,0.7)
    
       ## Labels
       if mol%dim2 == 0:
          ax.set_ylabel('Renormalized charges',fontsize=5)
       if mol > total_plots-dim2-1:
          ax.set_xlabel('FF charges',fontsize=5)

    else:
        molid += 1

plt.tight_layout()
plt.show()
quit()
