# CDGHJ Multipurpose cybersecurity tool
A python tool designed for multipurpose use

# Prerequisites
Before using this tool, ensure you have the following tools installed and properly configured on your system:

Python or Python3: Make sure Python is installed.

Nmap: install Nmap

OpenVAS: Install OpenVAS (now known as Greenbone Vulnerability Manager).

TShark: Install TShark.

Metasploit: Install Metasploit.

Python Libraries: Install necessary Python libraries using pip: 
pip install python-nmap
pip install requests


# Functionalities

This is a multipurpose tool that will provide the following functionalities:

1. Network Scanning: Discover live hosts and open ports using Nmap.
2. Vulnerability Scanning: Identify vulnerabilities in the network using OpenVAS.
3. Packet Capturing: Capture and analyze network traffic using TShark.
4. Penetration Testing: Perform exploitations using Metasploit.
   

# Functions:

1. network_scan(): Uses python-nmap to perform a network scan and display open ports and services.
2. vulnerability_scan(): Placeholder function to initiate a vulnerability scan using OpenVAS. Implementing full OpenVAS API interactions requires more detailed code and setup.
3. packet_capture(): Utilizes TShark to capture network packets for a specified duration and saves them to a file.
4. penetration_testing(): Launches the Metasploit console for manual penetration testing.
5. main_menu(): Provides a CLI menu for users to select desired functionalities.

# Usage:

Run the script using Python:

  python CDGHJ_MP_Tool.py      or        sudo python CDGHJ_MP_Tool.py
  # Note: In some case you might need to use sudo to elevate privilage for certain task/usage.

 # Important Notes
 
1. OpenVAS Integration:

The vulnerability_scan function provided is a simplified placeholder. Integrating OpenVAS (GVM) fully requires interacting with its API to create targets, initiate scans, retrieve reports, etc.
Refer to the Greenbone Vulnerability Management documentation for detailed API usage.

2. Metasploit Automation:

The current script launches the Metasploit console manually. For automation, consider using the msfrpc interface or Metasploit's console scripting capabilities.

3. Permissions:

Some operations, especially network scanning and packet capturing, may require administrative privileges. Run the script with appropriate permissions (e.g., using sudo on Unix-based systems).

4. Security Considerations:

Ensure that you have authorization to perform scans and penetration tests on the target systems to avoid legal issues.
Handle credentials securely, especially when interacting with tools like OpenVAS.

5. Error Handling:

The script includes basic error handling. Depending on your needs, you might want to enhance it to handle specific exceptions and edge cases.
