# TO DO:
# Find way to overwrite common-session with current file in /etc/pam.d/
# Find way to overwrite nsswitch.conf with current file in /etc/nsswitch.conf

import os
import sys
import getopt
from time import sleep

# checks the euid if the user is root
def update():
    os.system("sudo apt update && sudo apt upgrade -y")

def configure_ldap_client():
    os.system("apt install ldap-auth-config -y")
    # find way to modify files for NSS
    # find way to add line for manual logins
    # find way to setup automount
    # find way to export Dirs

def check_root() -> bool:
    if os.geteuid() != 0:
        return (False)
    else:
        return (True)

# updates the machine and installs the required drivers
def install_nvidia_drivers():
    os.system("sudo ubuntu-drivers autoinstall")

# installs gcc, g++ and cuda drives
def install_cuda_drivers():
    os.system("sudo apt install gcc g++ -y")
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb")
    os.system("sudo dpkg -i cuda-keyring_1.1-1_all.deb")
    os.system("sudo apt update")
    os.system("sudo apt install cuda -y")

# install ssh
def install_ssh():
    os.system("sudo apt install openssh-server")
    os.system("sudo systemctl enable ssh")

# clones gpu burn which stress tests graphics cards
def clone_gpu_burn():
    os.system("git clone https://github.com/wilicc/gpu-burn")
    print("GPU-Burn was cloned in current directory...")
    sleep(5)

def help():
    print("Usage: configurator.py <switch>")
    print("Switches:")
    print("----------------------")
    print("-h: Displays this message")
    print("-g: GPU Install")
    print("-n: Normal Install")
    print("----------------------")
    print("Normal Install")
    print("SSH")
    # need to add other parts from ubuntu checklist
    print("----------------------")
    print("GPU Install")
    print("SSH")
    print("Nividia Drivers")
    print("CUDA Drivers")
    print("GPU-Burn")

# components installed when dealing with GPU server
def gpu_server_install():
    generic_server_install()
    install_nvidia_drivers()
    install_cuda_drivers()
    clone_gpu_burn()

# components installed when dealing with a regular server
def generic_server_install():
    update()
    install_ssh()

def main():
    check_sudo = check_root()

    # remove first commandline arg
    if(check_sudo == False):
        print("ERROR: Are you sudo?")
    else:         
        argumentList = sys.argv[1:]

        options = "hgn"
        long_options = ["help", "gpu", "normal"]

        try:
            # Parse arguments
            arguments, values = getopt.getopt(argumentList, options, long_options)


            # checking each argument
            for currentArgument, currentValue in arguments:
        
                if currentArgument in ("-h", "--help"):
                    help()
                
                elif currentArgument in ("-g", "--gpu"):
                    print("GPU Config Selected...")
                    sleep(5)
                    gpu_server_install()

                elif currentArgument in ("-n", "--normal"):
                    print("Normal Config Selected...")
                    sleep(5)
                    generic_server_install()

        except getopt.error as err:
            # output error, and return with an error code
            print(str(err))

if __name__ == '__main__':
    main()