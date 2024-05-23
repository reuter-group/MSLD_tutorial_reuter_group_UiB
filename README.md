# Multisite &lambda; Dynamics
1. **Hardware requirements**  
   Linux system with NVIDIA GPU  
   **!! root or superuser privileges are NOT required !!**  
   
3. **Software requirements**  
   [CHARMM program](https://charmm.chemistry.harvard.edu/request_license.php?version=free)  
   [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)  
   PyMOL
    
 ## Compiling CHARMM ##
** You can follow the steps from the [pyCHARMM](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main/0Install_Tools/Linux) workshop as well, below is just a part of the things that are on the pyCHARMM workshop page
**

   1. Install Conda and create a new environment  
   ```conda create --name charmm```  
   ```conda activate charmm```  
   - install mamba within the conda environment to make the next steps fast   
   ```conda install conda-forge::mamba```
   - check the version of NVIDIA drivers  
   ```nvidia-smi ```
   - install cuda version that is compatible with your NVIDIA drivers  
   ```mamba install -y -c "nvidia/label/cuda-x.y.y" cuda```  
   ```mamba install -y -c conda-forge make cmake binutils fftw openmpi openmm sysroot_linux-64==2.17 readline==8.2 rdkit openbabel pymol-open-source```  
   ```mamba install -y -c conda-forge gcc==X.X gxx==X.X gfortran==X.X ```    
   3. **Compile CHARMM**
