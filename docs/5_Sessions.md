# 5. Runing jobs in the IBME cluster


## Batch Sessions 

In batch computing environments, jobs are submitted to compute nodes through the SLURM scheduler. SLURM ensures that the resources (GPUs, CPUs and Memory) are efficiently utilised across the cluster. It evaluates each job based on factors including requested runtime, required resources, and current cluster availability, then assigns priorities to determine job scheduling order.

## Submitting jobs using SLURM and Mamba

To submit the job to the compute node with the SLURM scheduler, the code to be run should be included in a shell script `(.sh)`. We have created an example shell script to work through the process and requirements of submitting the job to the compute node. Once connected to the IBME cluster, from the login node:

-   Create and activate a Mamba environment (you can also create a Python virtual environment). This is to ensure we are in an isolated environment and that the packages we install do not interfere with our other work in the cluster. 

    !!! terminal "code"
        ```bash
        $ mamba create --name ImageAnalysis
        $ mamba activate ImageAnalysis
        $ mamba install -c conda-forge matplotlib; mamba install -c conda-forge numpy
        ```

-   Make a directory, `cd` into the directory. The output of the jobs submitted through SLURM is saved in the directory where the jobs are submitted from. Therefore, it is recommended to create one directory per project and subdirectories to store job output each time a job is submitted.

    !!! terminal "code"
        ```bash
        $ mkdir Example_job
        $ cd Example_job
        ```

-   Download a shell and Python script file using the following command:

    !!! terminal "code"
        ```bash
        $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_script.sh
        $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_python.py
        ```

    The `Example_script.sh` contains the following code:

    !!! terminal "code"
        ```bash
        ##!/bin/bash
    
        echo "This job is running on:"
        hostname

        python3 Example_python.py
        ```

    The shell script can be thought of as a manual for the compute node. The compute node reads the shell script and runs the commands line by line sequentially. The first line of the script `#!/bin/bash` instructs the system to run the script as a `bash` shell. The second line of the script prints a message and the third line prints the hostname. The final line of the script runs the Python script `Example_python.py`. The Python script generates some random numbers, generates the plot and saves it as a `plot.png` file. 

-   The Python script requires some packages to run successfully. These are `matplotlib` and `numpy`. Install them using command: 

    !!! terminal "code"
        ```bash
        $ mamba install -c conda-forge matplotlib; 
        $ mamba install -c conda-forge numpy
        ```
 
-   Once the steps above have been followed, the job can be submitted using the following command: 

    !!! terminal "code"
        ```bash
        $ sbatch ./Example_script.sh
        ```

## Submitting jobs using SLURM and default module

The software installed on the HPC and available through the `module` package manager may run much faster than software installed using `mamba`. Jobs will use fewer resources and run more efficiently. Therefore, if a package available on the HPC meets the user's needs, it is recommended to use the packages already available on the HPC.

Once connected to the IBME cluster, submit the job using the default modules:

-   make a directory, `cd` into the directory. Output of the jobs submitted through SLURM are saved in the directory where the jobs is submitted from. Therefore, it is recommended to create a directory per project and sub-directories to store the job output everytime a job is submitted. 

    !!! terminal "code"
        ```bash
        $ mkdir Example_job
        $ cd Example_job
        ```
-   download a shell script file using command

    !!! terminal "code"
        ```bash
        $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_default_script.sh
        ```
     The `Example_script.sh` contains the following code:

    !!! terminal "code"
        ```bash
        ##!/bin/bash

        module load cuda
        nvcc --version

        echo "This job is running on node:"
        hostname

        echo "GPU in this node are:"
        nvidia-smi
        ```
    The second line of the script loads an HPC package using the module command, and the third line prints the package version. It is necessary to load the module at the beginning if it will be used later in this script or in any other scripts invoked by it. The script then prints a message on the third line, followed by the hostname on the fourth line. The fifth line prints another message, and the final line displays information about the NVIDIA GPUs.

-   Once the steps above have been followed, the job can be submitted using the following command:

    !!! terminal "code"
        ```bash
        $ sbatch ./Example_default_script.sh
        ```


## The job Output

The job output is not printed in the terminal, instead it is saved in a file called `slurm-JOBID.out` in a directory where we submitted the job from. The `JOBID` in the file name is an unique ID assigned by SLURM to every job. The ouput of the can be investigated using command `less` or `cat`. In the example below, we have used the `less` commnd which opens the page in a interactive mode on the screen. In the example below we have shown the job output of SLURM with mamba, if you have followed the example above you should see:

!!! terminal "code"
    ```bash
    $ less slurm-JOBID.out 
    ```

    ```bash
    This job is running on:
    node04
    ```
    it can be node05 depending on the availability of the node. 

The job also outputs a plot called `plot.png` file, this is also stored in the directory where the job is submitted from. The HPC systems are remote machines which don't have a graphical user interface. It is recomemded to transfer this file to the local computer using FileZZile or rsync command, see [chapter 2](http://127.0.0.1:8000/IBME_Cluster2_Transferring_files_to_remote_machine/) for more details.

## The job Option configaration

SLURM jobs can be configured to run with several specific options. These options can be specified at the top of the shell script with `#SBATCH` keyword followed by the option name and its value. The option names can either be as a short or long format. The table below highlights some of the common options:

<div style="display: flex; justify-content: center;" markdown="1">

| **Short**                                         | **Long** | **Description** |
|:---------------------------------------------------|:-------------| :-------------|
|-D |  --chdir | Working directory for the job, if not specified jobs will be submitted from the corrent working directory |
|-o |  --output| Location where the output will be saved - needs specifyinh only if the output need to be saved somewhere else) |
|-A | --account| Billing account |
|-p | --partition| partition - currently the IBME cluster has onle one partition called standared |
|-c | --cpus-per-task| number of cpus needed for the job |
|-t | --time| Runtime limit |
|-J | --job-name| Job name |
|  | --gpus| number of gpus needed for the job - maximum limit for IBME cluster is 1 |
|  | --mem| RAM required for the job |

</div>

For example to request a 2 cpus, 1 gpu, 4GB of memory and 10 minutes of runtime, the following `#SBATCH` notion can be used before any command to be run in the cluster

!!! terminal "code"
    ```bash
    #!/bin/bash
    #SBATCH -c 4
    #SBATCH --gpus=1
    #SBATCH --mem=4G
    #SBATCH -t 00:10:00 # time for the job HH:MM:SS.

    echo "This job is running on node:"
    hostname

    echo "CPU requested:"
    echo $SLURM_CPUS_PER_TASK

    echo "Memory per node:"
    echo $SLURM_MEM_PER_NODE

    ```



SLURM automatically creates some environmental variables of the options specified through `#SBATCH`. For instance `$SLURM_CPUS_PER_TASK` and `$SLURM_MEM_PER_NODE` variable stores the number of cpu and memory requested. If the shell script above is submitted it will output, the nodename andthe cpu and memory requested. The IBME cluster doesn't automatically export the number of gpu and time into environment variable. To confirm whether this resources were allocated `scontrol` command can be used. The `scontrol` command only works for running or recently queued jobs.

!!! terminal "code"
    ```bash
    $ scontrol show job ID 
    
    shows a lot of information specific to the job. To filter and see information specific to gpu the following command can be used

    $ scontrol show job ID | grep -i gres

    To filter and see information specific to time the following command can be used

    scontrol show job ID | grep -i TimeLimit

    ```

The `sacct` command provides a lot of useful information abouth the job that has completed. However this command is not supported in the IBME cluster. 



## Interactive Sessions

The IBME cluster also allows tO run interactive sessions. The `srun` command can be used to allocate the specific recourses and starts an interactive shell on the compute node based on the resources. To start an interactive session on the IBME cluster, the following command can be used:


!!! terminal "code"
    ```bash
    $ srun --pty bash
    ```

    The `--pty bash` command provides and interactive shell
    
    once the session starts the host of terminal prompt will change to show the name of the compute node

    ```bash
    $ `[<userid>@node05 ~]$`
    ```


In the example above an interactive session starts but doesn't request any specific memory. By default only 2 cpus and a runtime of 4 days are attached to the session. To request specific resources in terms of cpu, gpu, memory and runtime the following command can be used:

!!! terminal "code"
    ```bash
    $ srun --gpus=1 --cpus-per-task=4 --mem=4G --time=4:00:00 --pty bash
    ```

   - `--gpus` options request gpus (1 in this case)
   - `--cpus-per-task` options request cpus (4 in this case)
   - `--mem` options request RAM (4GB in this case)
   - `--time` options request time limit for th session (4 hours in this case)

One in the interactive session run `echo $SLURM_JOB_ID` to see the Job ID associated with the session. To see information about the resources and other information regarding the session use command:

!!! terminal "code"
    ```bash
    $ scontrol show job ID
    ```
    Filter and search for cpu, gpu, memory and timelimit for the session.


