import sys
import numpy as np
import matplotlib.pyplot as plt

ligPath = sys.argv[1]
sub1 = sys.argv[2]
sub2 = sys.argv[3]

# Load energies
## Forward direction
ffE1 = np.loadtxt(f'{ligPath}crn2ffwater/ff.ener',dtype=float, skiprows=1, usecols=1)
crnE1 = np.loadtxt(f'{ligPath}/crn2ffwater/renormal.ener',dtype=float, skiprows=1, usecols=1)

## Backward direction
crnE2 = np.loadtxt(f'{ligPath}/water/renormal.ener',dtype=float, skiprows=1, usecols=1)
ffE2 = np.loadtxt(f'{ligPath}/water/ff.ener',dtype=float, skiprows=1, usecols=1)

# difference always, final - initial
frwd = np.subtract(crnE1,ffE1)
bcwd = np.subtract(ffE2,crnE2)

plt.hist(frwd, bins=50, density=True, label='FF -> CRN')
plt.hist(-bcwd, bins=50, density=True, label='CRN -> FF')
plt.title(f'Energy Difference Distributions for FF and CRN Ensembles for Ligand s1s{sub1}.s2s{sub2} in water')
plt.xlabel(r'$\Delta$U (kcal/mol)',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.legend()
#plt.show()
plt.tight_layout()


plt.show()
