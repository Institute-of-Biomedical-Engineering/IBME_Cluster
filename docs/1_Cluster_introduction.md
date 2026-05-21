# 1. IBME Cluster introduction

## Accessing the cluster

The IBME cluster is dedicated to IBME users only. Access to the cluster can be requested by raising a ticket with the IBME Hub at **ibmehub@eng.ox.ac.uk**. Approval usually takes up to 10 working days. Once approved, the user is provided with a username and a temporary password, which must be changed on first login.


## Cluster layout

The IBME cluster consists of several components connected together in a network and works as a unified system.


<p align="center">
    <img src="../images/IBME Cluster.png" width="720">
</p>

## Key Components

The core components of the cluster include:

 - **Lonin None:** The login node is a computer where users land when they first log in to the IBME cluster. The login node for the IBME cluster runs Rocky Linux (based on Red Hat Enterprise Linux). Logging in to the IBME cluster can be accomplished using the command `ssh <userid>@engs-ibmecluster01.eng.ox.ac.uk` from an IBME office computer on the wired office network, or after remotely connecting to your IBME office computer. To connect to the cluster remotely via VPN, the command `ssh -L 7719:localhost:22 -J <userid>@ibme-ssh-gateway.eng.ox.ac.uk <userid>@engs-ibmecluster01.eng.ox.ac.uk` can be used.

    After a successful login, the terminal prompt changes to `[<userid>@lnode01 ~]$`, and the user is placed in their home directory at `/users/<userid>`. The login nodes can be used for tasks such as viewing and editing files, building software environments, navigating the file system, and transferring or downloading files. However, login nodes should not be used for compute-intensive tasks. The user’s home directory is typically limited in storage capacity; therefore, data intended for computation should instead be stored in `/data/<userid>`.


!!! info
    The `<userid>` must be replaced with the user name.

    For the **first-time login**, the user will be prompted for two passwords. The first password is the user’s Engineering Department (Eng domain) password used at the IBME. The second password is the temporary cluster password provided in the approval email from the IBME Hub. During the initial login, the cluster authentication system will require the temporary password to be changed. After the password has been updated, the terminal session may disconnect automatically. If this happens, simply reconnect using the SSH command shown above and log in again. This time, use the newly updated cluster password as the second password.

    For all subsequent logins, the user will be required to enter only their second password (the one updated by the user) for authentication.



- **Head None:** To submit jobs to the compute nodes, the user must first log in to the head node. The command to log in to the head node is `ssh headnode01`. Once logged in, the terminal prompt changes to `[<userid>@headnode1 ~]`.

    The head node in the IBME cluster runs CentOS Linux (based on Red Hat Enterprise Linux) and hosts the SLURM scheduler, which users can use to submit jobs to the compute nodes. Instructions on how to use SLURM in the IBME cluster are provided in the [Batch and interactive sessions section](http://127.0.0.1:8000/IBME_Cluster/5_Sessions/).

    Pre-installed software on the IBME cluster is available from the head node. See the [Module and packages](http://127.0.0.1:8000/IBME_Cluster/4_Modules_packages/) section for instructions on how to access or install software.

    The file system on the login node is the same as that of the head node. As a result, files and data stored in `/users/<userid>` and `/data/<userid>` on the login node are also accessible from headnode1.


!!! info
    During the **first-time login**, the user will be prompted to enter the temporary password provided in the approval email from IBME Hub. The authentication system will then require the temporary password to be changed. Choose a secure password to complete the setup. For all subsequent logins, only the new password set by the user will be required for authentication.


- **Compute Node:** Compute nodes are the machines responsible for executing jobs on the cluster. Users do not have direct access to the compute nodes (for example, commands such as `ssh computenode` are not permitted). Jobs can only be submitted from the head node (headnode1) using SLURM, as described above.

    The IBME cluster consists of two identical compute nodes. Each node is equipped with **10 x [Tesla V100](https://www.nvidia.com/en-gb/data-center/tesla-v100/) 32GB GPU** and **2 x Intel Xeon Gold 5118 (12 core) 2.30GHz CPU**. Each CPU supports two threads per core, resulting in **24 physical CPU cores and 48 logical CPUs per node**. In addition, each node has **190 GB** of system RAM (separate from GPU memory).

    The table below summarises the compute infrastructure available on each node


<div style="display: flex; justify-content: center;" markdown="1">


| **Type**                                         | **Configuration** | 
|:---------------------------------------------------|:-------------|
|GPU| 20 x Tesla V100 32GB|
|CPU| 4 x Intel Xeon Gold 5118 (12 core)|
|RAM| 190 GB (per-node)|

</div>