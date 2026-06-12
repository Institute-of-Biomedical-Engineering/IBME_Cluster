# 5. Running jobs in the IBME cluster


## Batch Sessions 

In batch computing environments, jobs are submitted to compute nodes through the SLURM scheduler. SLURM ensures that the resources (GPUs, CPUs and memory) are efficiently utilised across the cluster. It evaluates each job based on factors including requested time limit, required resources, and current cluster availability, then assigns priorities to determine job scheduling order.

## Submitting jobs using SLURM and Mamba

To submit a job to a compute node via the SLURM scheduler, your commands must be included in a shell script (a `.sh` file). We have created an example script to walk you through the submission process and its requirements. Once you are connected to the IBME cluster, run the following commands from the login node:

-   Create and activate a Mamba environment (alternatively, you can also create a Python virtual environment). This is to ensure we are in an isolated environment and that the packages we install do not interfere with our other work in the cluster. 

    !!! terminal "code"
        ```bash
        $ mamba create --name ImageAnalysis
        $ mamba activate ImageAnalysis
        ```

-   Make a directory and `cd` into it. Because SLURM saves job output in the directory from which the jobs are submitted, it is recommended to create a dedicated directory for each project, along with specific subdirectories to organize the output of each job.

    !!! terminal "code"
        ```bash
        $ mkdir Example_job
        $ cd Example_job
        ```

-   Download the shell and Python script files using the following commands:

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

    The shell script acts as a manual for the compute node, which reads the file and executes the commands sequentially, line by line. The first line (`#!/bin/bash`) instructs the system to run it using the Bash shell. The second and third lines print a custom message and the system's hostname. Finally, the script executes `Example_python.py`, which generates random numbers, creates a plot, and saves it as a `plot.png` file.

-   To run successfully, the Python script requires the `matplotlib` and `numpy` packages. Install them using this command:

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

Software available through the HPC module system often runs significantly faster and more efficiently than software installed via `mamba`. Utilising these native modules helps jobs consume fewer cluster resources. Therefore, if a pre-installed package meets your needs, it is highly recommended to use it.

Once connected to the IBME cluster, submit the job using the default modules:

-   Make a directory and `cd` into it. Because SLURM saves job output in the directory from which the jobs are submitted, it is recommended to create a dedicated directory for each project, along with specific subdirectories to organize the output of each job.

    !!! terminal "code"
        ```bash
        $ mkdir Example_job
        $ cd Example_job
        ```
-   Download the shell script file using the following command:

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

        echo "GPUs in this node are:"
        nvidia-smi
        ```
    The second line of the script loads an HPC package using the `module` command, and the third line outputs its version. It is necessary to load the module at the beginning if it will be used later in this script or in any other scripts invoked by it. The script then prints a message on the fourth line, the hostname on the fifth, another message on the sixth, and finally displays information about the NVIDIA GPUs.

-   Once the steps above have been followed, the job can be submitted using the following command:

    !!! terminal "code"
        ```bash
        $ sbatch ./Example_default_script.sh
        ```


## The job output

Instead of printing to the terminal, SLURM saves job output to a file named `slurm-JOBID.out` in the submission directory. The `JOBID` in the file name is a unique ID assigned by SLURM to every job. The output can be investigated using command `less` or `cat`. The example below uses the `less` command, which opens the file in an interactive viewer. If you followed the previous Mamba environment example, your output should look like this:

!!! terminal "code"
    ```bash
    $ less slurm-JOBID.out 
    ```

    ```bash
    This job is running on:
    node04
    ```
    It can be node05 depending on the availability of the nodes. 

The job also generates a plot named plot.png, which is stored in the directory from which the job was submitted. Because HPC systems are remote machines without a graphical user interface (GUI), you cannot view this image directly on the cluster. It is recommended to transfer the file to your local computer using FileZilla or the rsync command; see [topic 2](https://institute-of-biomedical-engineering.github.io/IBME_Cluster/2_Transferring_files_to_remote_machine/) for more details.

## The job option configuration

SLURM jobs can be configured to run with several specific options. These options can be specified at the top of the shell script using the `#SBATCH` keyword, followed by the option name and its value. The option names can either be as a short or long format. The table below highlights some of the common options:

<div style="display: flex; justify-content: center;" markdown="1">

| **Short**                                         | **Long** | **Description** |
|:---------------------------------------------------|:-------------| :-------------|
|-D |  --chdir | Working directory for the job. if not specified jobs will be submitted from the current working directory |
|-o |  --output| File path for saving job output (only required if saving to a non-default location) |
|-A | --account| Billing account name |
|-p | --partition| Partition name (currently the IBME cluster has only one partition called standard) |
|-c | --cpus-per-task| Number of CPUs requested per task |
|-t | --time| Maximum runtime limit |
|-J | --job-name| Job name |
|  | --gpus| Number of GPUs requested for the job (maximum limit for IBME cluster is 1) |
|  | --mem| Amount of RAM required for the job |

</div>

For example, to request 2 CPUs, 1 GPU, 4 GB of RAM, and a 10-minute time limit, add these #SBATCH directives to the top of your script before any commands:

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


SLURM automatically creates several environment variables based on the options specified via `#SBATCH`. For instance, the `$SLURM_CPUS_PER_TASK` and `$SLURM_MEM_PER_NODE` variables store the number of requested CPUs and the allocated memory. If the example shell script above is submitted, it will output the node name along with these requested CPU and memory values. Note that the IBME cluster does not automatically export the number of GPUs or the time limit into environment variables. To confirm whether these specific resources were successfully allocated, you can use the `scontrol` command. The `scontrol` command only works for running or recently queued jobs.

!!! terminal "code"
    ```bash
    $ scontrol show job ID 
    
    This command displays a significant amount of job-specific information. To filter and view information specific to GPU the following command can be used

    $ scontrol show job ID | grep -i gres

    To filter the output and view details specific to the time limit, you can use the following command:

    $ scontrol show job ID | grep -i TimeLimit

    ```

The `sacct` command provides useful information about completed jobs. However, this command is not supported on the IBME cluster.



## Interactive sessions

The IBME cluster also allows users to run interactive sessions. The `srun` command can be used to allocate the specific resources and start an interactive shell on the compute node based on the resources. To start an interactive session on the IBME cluster, the following command can be used:


!!! terminal "code"
    ```bash
    $ srun --pty bash
    ```

    The `--pty bash` command provides an interactive shell
    
    Once the session starts, the hostname in your terminal prompt will change to show the name of the compute node.

    ```bash
    [<userid>@node05 ~]$
    ```


The example above launches an interactive session without specifying memory requirements. By default, SLURM allocates only 2 CPUs and a 4-day time limit. To request custom CPU, GPU, memory, or time limit configurations, use the following command:

!!! terminal "code"
    ```bash
    $ srun --gpus=1 --cpus-per-task=4 --mem=4G --time=4:00:00 --pty bash
    ```

   - `--gpus` option requests GPUs (1 in this case)
   - `--cpus-per-task` option requests CPUs (4 in this case)
   - `--mem` option requests RAM (4GB in this case)
   - `--time` option sets the time limit for the session (4 hours in this case)

Once inside the interactive session, run echo $SLURM_JOB_ID to see the Job ID assigned to it. To view resource allocations and other details regarding the session, use the following command:

!!! terminal "code"
    ```bash
    $ scontrol show job ID
    ```
    Filter and search for cpu, gpu, memory and time limit for the session.


