import os, sys

import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign

import Mol2writer

p = AllChem.ETKDGv2()
p.verbose = False


sdfs = Chem.SDMolSupplier('ligands.sdf', removeHs=False)

out=00

for sdf in sdfs:
	mol = sdf
	try:
		os.remove(f'mol{out}.mol2')
	except FileNotFoundError:
		None
	Mol2writer.MolToMol2File(mol, f'mol{out}.mol2', confId=-1)
	os.system(f'python rename_atoms.py mol{out}.mol2')
	out += 1

