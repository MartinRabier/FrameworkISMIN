# Framework Panhelleux Bonnet Rabier

This project is an implementation of different tools to discover network security. It includes various functionalities to help analyze and secure networks.

## Features

- **Footprint**: Get information about a website host or the website code
- **Network Scanning**: Perform a full scan of the network to determine open and / or vulnerable ports
- **Enumeration**: Grab banners and enumerate different OSs or users present on the targeted network
- **Gainning Access**: Exploit various breaches thanks to tools such as hydra, nmap and metasploit framework
## Installation

To install the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone -b main --single-branch https://github.com/MartinRabier/FrameworkISMIN.git
    ```
2. run the file :
   ```sh
   Framework.py
   ```

## Usage

Before lauching the project be sure to install the following python modules using pip install
```sh
subprocess ; time ; python-nmap ; python-whois ; bs4 (beautifulsoup) ; ftplib ; socket ; ipaddress ; psutil 
```
Most of these tools are usually pre-installed on casual python environment but it's better to check before use.
Also, be sure to have the following tools installed on your computer (using sudo apt install or snap install for latest versions) :
```sh
Nmap, Hydra, Metasploit-framework
```
To launch the project you just need to run the file **Framework.py** and follow the instructions displayed in the terminal.

Tools featured in the **"Footprint** part require an internet access to run whois and beautiful soup, every other tools can be run with a bridged connection to a vulnerable machine


