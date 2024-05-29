import sys
import numpy as np
from scipy.spatial.distance import cdist

# Load the data from the first file
file1 = sys.argv[1]
data1 = np.genfromtxt(file1, dtype=str)

# Load the data from the second file
file2 = sys.argv[2]
data2 = np.genfromtxt(file2, dtype=str)

# Extract the identifiers and coordinates from the first file
identifiers1 = data1[:, 0]
coords1 = data1[:, 1:].astype(float)

# Extract the identifiers and coordinates from the second file
identifiers2 = data2[:, 0]
coords2 = data2[:, 1:].astype(float)

# Calculate the RMSD for each line in file 1 corresponding to all lines in file 2
rmsd_values = cdist(coords1, coords2, 'euclidean')

## Print the lowest RMSD and corresponding identifier in file 2 for each line in file 1
#for i in range(len(rmsd_values)):
#    min_rmsd_index = np.argmin(rmsd_values[i])
#    min_rmsd = rmsd_values[i, min_rmsd_index]
#    matching_identifier = identifiers2[min_rmsd_index]
#    print(f"Line {i+1} in File 1 --> Lowest RMSD: {min_rmsd:.4f}, Identifier in File 2: {matching_identifier}")


# Print the lowest RMSD, identifier from file 1, and corresponding identifier from file 2 for each line in file 1
for i in range(len(rmsd_values)):
    min_rmsd_index = np.argmin(rmsd_values[i])
    min_rmsd = rmsd_values[i, min_rmsd_index]
    matching_identifier1 = identifiers1[i]
    matching_identifier2 = identifiers2[min_rmsd_index]
    print(f"Line {i+1} in File 1 --> Identifier: {matching_identifier1}, Lowest RMSD: {min_rmsd:.4f}, Identifier in File 2: {matching_identifier2}")
