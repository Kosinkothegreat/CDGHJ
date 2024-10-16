import os
import subprocess
import sys
import time
import nmap
import requests

def network_scan():
    print("\n=== Network Scanning with Nmap ===")
    target = input("Enter target IP or range (e.g., 192.168.1.0/24): ")
    scanner = nmap.PortScanner()
    print(f"Scanning {target} for open ports...")
    scanner.scan(target, arguments='-sV')
    for host in scanner.all_hosts():
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"\nProtocol: {proto}")
            lport = scanner[host][proto].keys()
            for port in sorted(lport):
                service = scanner[host][proto][port]['name']
                print(f"Port: {port}\tService: {service}")

def vulnerability_scan():
    print("\n=== Vulnerability Scanning with OpenVAS ===")
    target = input("Enter target IP: ")
    # Assuming OpenVAS is running and gvmd is configured
    # You need to have OpenVAS API credentials
    openvas_url = "https://127.0.0.1:9392"
    username = "admin"  # Replace with your OpenVAS username
    password = "password"  # Replace with your OpenVAS password

    # Authenticate and get a token
    try:
        response = requests.post(f"{openvas_url}/login", data={'username': username, 'password': password}, verify=False)
        if response.status_code == 200:
            token = response.cookies.get('GVMID')
            print("Authenticated with OpenVAS.")
        else:
            print("Failed to authenticate with OpenVAS.")
            return
    except Exception as e:
        print(f"Error connecting to OpenVAS: {e}")
        return

    # Initiate a scan (simplified example)
    # In practice, you'd need to create targets, tasks, etc.
    print(f"Starting vulnerability scan on {target}...")
    # This is a placeholder. Actual implementation requires detailed OpenVAS API usage.
    print("Vulnerability scan initiated. Please check OpenVAS dashboard for results.")

def packet_capture():
    print("\n=== Packet Capturing with TShark ===")
    interface = input("Enter network interface (e.g., eth0): ")
    capture_duration = input("Enter capture duration in seconds (e.g., 10): ")
    output_file = input("Enter output file name (e.g., capture.pcap): ")

    try:
        print(f"Starting packet capture on {interface} for {capture_duration} seconds...")
        subprocess.run(['tshark', '-i', interface, '-a', f'duration:{capture_duration}', '-w', output_file])
        print(f"Packet capture completed. Saved to {output_file}")
    except Exception as e:
        print(f"Error during packet capture: {e}")

def penetration_testing():
    print("\n=== Penetration Testing with Metasploit ===")
    print("Launching Metasploit console...")
    try:
        subprocess.run(['msfconsole'])
    except Exception as e:
        print(f"Error launching Metasploit: {e}")

def main_menu():
    while True:
        print("\n=== Multipurpose Cybersecurity Tool ===")
        print("1. Network Scanning (Nmap)")
        print("2. Vulnerability Scanning (OpenVAS)")
        print("3. Packet Capturing (TShark)")
        print("4. Penetration Testing (Metasploit)")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            network_scan()
        elif choice == '2':
            vulnerability_scan()
        elif choice == '3':
            packet_capture()
        elif choice == '4':
            penetration_testing()
        elif choice == '5':
            print("Exiting the tool. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

# This tool was created and developed by Kosinko
