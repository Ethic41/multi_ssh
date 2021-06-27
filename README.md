# Multi_SSH

Multi_SSH started as a challenge posed to me by my mentor (OBC) to create a script that can ssh into multiple servers concurrently and execute a list of commands, 3 hours later this python project was born

# Setup Project
## The project was built with Python 3.8, but Python 3.6 or later should work
### 1 - Clone the project
```bash
# clone the project
git clone https://github.com/Ethic41/multi_ssh.git

# change into project directory
cd multi_ssh
```
### 2 - First create a virtual environment (NB: this step is optional)
```bash
# create virtual env
python -m venv multi_ssh_env

# activate virtual environment
source multi_ssh_env/bin/activate
```
### 3 - Install Requirements
```bash
python -m pip install -r requirements.txt
```
# How to use
### multi_ssh requires to two input files:
* servers list file - contains list of servers and their credentials
* commands list file - contains commands to be executed on various ssh servers

sample of the files can be found in the ```sample_files``` directory

The servers list file must be in the format of ```sample_files/sample_servers_list.dmd``` file, but the name of the file can be anything you want and can be in any readable directory, just make sure to provide the full file path if the file is in a different directory from ```multi_ssh.py```

* username (mandatory) - is the name of the user you are connecting as
* host_address (mandatory) - is the host server address
* password (optional) - the server password, if any
* ssh_key (optional) - is a string of the actual ssh_key if any
* ssh_key_file (optional) - is the full file path of the ssh key if any
* port (optional) - default is 22, but you can override with your custom port

The commands list is just a normal shell script file, it assumes commands are line separated, but basically you can do anything you would in a normal shell e.g bash

NB: if you do not specify servers file or command files the default sample files are used

# Demo
