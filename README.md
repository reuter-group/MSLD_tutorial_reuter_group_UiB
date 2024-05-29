# Multisite &lambda; Dynamics
1. **Hardware requirements**  
   Linux system with NVIDIA GPU  
   **!! root or superuser privileges are NOT required !!**  
   
2. **Software requirements**  
   [CHARMM program](https://charmm.chemistry.harvard.edu/request_license.php?version=free)  
   [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)   
   PyMOL  
   [MMTSB](https://github.com/mmtsb/toolset)  
   [LOMAP](https://github.com/OpenFreeEnergy/Lomap) -- Optional  

4. **References literature**
   - [&lambda;D original paper](https://doi.org/10.1063/1.472109)
   - [MS&lambda;D paper](https://doi.org/10.1021/ct200444f)
   - [Adaptive Landscape Flattening (ALF)](https://doi.org/10.1021/acs.jpcb.6b09656)
   - [Protein Mutations - I](https://doi.org/10.1002/pro.3500)
   - [Protein Mutations - II](https://doi.org/10.1002/jcc.26525)
   - [Biasing potential replica exchange (BPREX)](https://doi.org/10.1021/ct500894k)
   - [msld_py_prep and charge corrections](https://doi.org/10.1021/acs.jcim.2c00047)
   - [MS&lambda;D benchmark paper](https://doi.org/10.1021/acs.jctc.0c00830)
   - [AMBER & OPLS in MS&lambda;D](https://doi.org/10.1021/acs.jcim.3c01949)
   - [FEP analysis guidelines](https://doi.org/10.1007/s10822-015-9840-9)  
   - [Best practices FEP](https://livecomsjournal.org/index.php/livecoms/article/view/v2i1e18378)  
   - [MBAR](https://arxiv.org/abs/1704.00891)
   - [charge changing mutations](https://pubs.acs.org/doi/10.1021/ct900565e)
   - [charge changing mutations FEP+](https://doi.org/10.1016%2Fj.jmb.2019.02.003)

5. **Github Resources**
   - [ALF](https://github.com/RyanLeeHayes/ALF)
   - [pyCHARMM workshop](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main)
   - [MS&lambda;D workshop](https://github.com/BrooksResearchGroup-UM/MSLD-Workshop)
   - [protein ligand benchmark datasets](https://github.com/openforcefield/protein-ligand-benchmark)
   - [protein tutorial](http://pmx.mpibpc.mpg.de/summerSchool2020_tutorial1/index.html)
   - [precomputed mutation free energies](http://pmx.mpibpc.mpg.de/tripeptide.html)

   
 ## Compiling CHARMM ##
** You can follow the steps from the [pyCHARMM](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main/0Install_Tools/Linux) workshop as well, below is just a part of the things that are on the pyCHARMM workshop page
**

   1. Install **miniconda** and create a new environment  
   ```conda create --name charmm```  
   ```conda activate charmm```  
   - install mamba within the conda environment to make the next steps fast   
   ```conda install conda-forge::mamba```
   - Please see more info on [pyCHARMM workshop's page](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main/0Install_Tools/Linux#1a-create-a-conda-environment-manually) regarding cuda and GCC  
      - check the version of NVIDIA drivers  
      ```nvidia-smi ```  
      - install cuda version that is compatible with your NVIDIA drivers  
         ```mamba install -y -c "nvidia/label/cuda-x.y.y" cuda```  
      - use GCC version that is recommended for your cuda version  
        ```mamba install -y -c conda-forge gcc==X.X gxx==X.X gfortran==X.X ```    
   - a few more packages through conda  
   ```mamba install -y -c conda-forge make cmake binutils fftw openmpi openmm sysroot_linux-64==2.17 readline==8.2 rdkit openbabel pymol-open-source pymbar```  

   2. **Compile CHARMM**
   - active your conda environment  
     ```conda activate charmm```  
   - untar CHARMM  
     ```tar -xvf charmm.tgz```  
     ```cd charmm```  
     ```mkdir build_charmm ```  
     ```cd build_charmm```  
     ```../configure -u --with-blade --without-mkl```  
     I'm using 8 cores (see next command) to compile/build charmm, you can use more cores eg. 10 or 20  or less eg 1 or 4.  
     ```make -j 8 all```  
**DONE**
