# 4. Moduels in the Cluster

## Pre-installed software

There are a few softwares that are pre-installed on the IBME cluster that are available to the users. The GPU software stack in the modules are:

| **Name**                                         | **Version** | **Description** |
|:---------------------------------------------------|:-------------| :-------------|
|CUDA |  `10.0.130`,    `10.1.243`,    `11.3.0`,    `11.8.0` | NVIDIA CUDA Toolkit |
|cuDNN |  `6.0.20`,    `7.0.1`,    `7.5.0`| CUDA Deep Neural Network Library |
|NCCL | `1.3.5`,    `2.1.2`,    `2.3.7`,    `2.4.2`| NVIDIA Collective Communications Library. |

The rest of the modules are for infrastructure/support that help the cluster environment work. One in the headnode1, the `module` tools can be used to view or interact with the modules. For exaample:

- The `module avail` or `module spider` command shows the available module in the system
- The `module load <module_name-version>` loads a module. (Note: replace the module_name and version to load a specific module)
- The `module unload <module_name-version>` unloads a module.
- The `module list` command shows the loaded module

Once the module is loaded it is automatically added to the PATH variable, which can be checked with the `echo $PATH` commans.

!!! terminal "code"
    ```bash
    $ module load cuda/10.0.130
    $ echo $PATH
    /usr/local/cuda-10.0/bin
    ```

## The Mamba or Conda package manager

As the available packages are limited, there may be situations where additional software needs to be installed. The Mamba package manager is one way to install additional software. Mamba is a faster successor to Conda and can be used interchangeably with Conda in most commands. Mamba is an open-source alternative to Conda, implemented in C++ to provide improved performance and faster dependency resolution.

With Mamba different version of the same software can be installed in the HPC (or other machines) which are organised in virtual environments. The software can be installed locally on HPC without needing the permission of the IBME HPC admin. 

## Installing Mamba on the IBME cluster

Before using Mamba on the IBME cluster it must be installed (Mamba is already preinstalled on the BMRC cluster). Follow the steps below to install Mamba on the IBME cluster. 

- Login to the IBME cluster - `ssh <userid>@engs-ibmecluster01.eng.ox.ac.uk`

- In the login node make a shell variable `dir="/users/<userid>/miniforge3"`


- Download the installer using `wget`. Information about the installer is available on the official GitHub [**page**](https://github.com/conda-forge/miniforge/)

 !!! terminal "code"
    ```bash
    $ wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    ```
    Once the installer has been downloaded, it will be available in the current directory as `Miniforge3-Linux-x86_64.sh`

- Run the installer and save the installed packages in the `miniforge3` directory

 !!! terminal "code"
    ```bash
    $ bash Miniforge3-$(uname)-$(uname -m).sh -b -p $dir
    ```

- Modify the shell configuration for Mamba

!!! terminal "code"
    ```bash
    $ dir/bin/mamba shell init --shell bash
    ```

- Restart the terminal by logining out and in of the IBME cluster. 

- Run the following commands to installs software repository (which are called channels) for Mamba

!!! terminal "code"
    ```bash
    $ conda config --add channels nodefaults
    $ conda config --add channels bioconda
    $ conda config --add channels conda-forge
    $ conda config --set channel_priority strict
    ```
- Check the repositories are installed 

!!! terminal "code"
    ```bash
    $ mamba config list channels
    channels:
        - conda-forge
        - bioconda
        - nodefaults
    ```

    nodefaults: means do not use the official Anaconda defaults channe
    conda-forge: largest community-maintained channel
    bioconda: Specialised channel for bioinformatics


## Installing software on the IBME cluster

To install software on the IBME cluster using Mamba a software environment (e.g. ImageAnalysis) must be created and activated. This can be created using command:

!!! terminal "code"
    Create environment

    ```bash
    $ mamba create --name ImageAnalysis
    ```
    Activate environment

    ```bash
    $ mamba activate ImageAnalysis
    ```
Once activated the environment name will appear in bracket - (ImageAnalysis). Look for the software to install from the repository, for example the [conda-forge](https://conda-forge.org/packages/?) repository. In the example below `CUDA` software will be installed from conda-forge [repository](https://anaconda.org/channels/conda-forge/packages/cuda/overview) in the software environment:

!!! terminal "code"
    ```bash
    $ mamba install conda-forge::cuda
    ```

We will not specify a specific version for the installation, as a result, Mamba will install the latest available package this is compatible on the IBME cluster system, which in this case was *CUDA 12.6.3*. This is not the latest version of CUDA but is a lot newer that the latest installed in the IBME cluster. 

The command above also installs many other CUDA related software packages, which are not available in latest version available in the IBME cluster. For example the `nvcc` and `gcc` compiler. 

The mamba environment can be deactivated using command:

!!! terminal "code"
    ```bash
    $ mamba deactivate ImageAnalysis
    ```


!!! info
    Installing software using Mamba also installes a large number of dependencies. Creating many software environments and installing softwares withing them can quickly fill up the the user's home directory. Therefore it is advisable to archive the software environment when its not needed. The software environments are located in `/users/<userid>/miniforge3/envs`.



