# WiFi Multi-Tasking Penetration Tool

## Disclaimer

The use of this tool is strictly for educational and ethical hacking purposes only. The author of this tool does not endorse or condone any illegal activities. Unauthorized access to or testing of networks without proper authorization is illegal and unethical. Always obtain explicit permission before testing or analyzing any network. The author and contributors are not responsible for any misuse or illegal activities conducted using this tool.

By using this tool, you agree to abide by all applicable laws and regulations and take full responsibility for your actions.


## Description

This Python script provides a suite of tools for WiFi penetration testing. It allows users to perform various attacks and network analysis tasks using a command-line interface. The script leverages common tools like `airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`, `reaver`, `airbase-ng`, and `ettercap` to perform tasks such as network scanning, handshake capturing, deauthentication attacks, password cracking, WPS attacks, Evil Twin attacks, and MITM attacks.

## Features

- Display available wireless interfaces
- Start and stop monitor mode on a wireless interface
- Scan for available networks
- Capture WPA/WPA2 handshakes
- Perform deauthentication attacks
- Crack WPA/WPA2 passwords
- Conduct WPS attacks
- Create Evil Twin access points
- Execute MITM attacks

## Requirements

- Python 3
- `airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`, `reaver`, `airbase-ng`, and `ettercap` installed
- GNOME Terminal (for executing commands in new terminal windows)
- `sudo` access

## Installation

   Clone this repository:
   ```sh
   1:- git clone https://github.com/yourusername/wifi-multi-tasking-penetration-tool.git
   2:- cd Directory
   3:- sudo apt update
   4:- sudo apt install aircrack-ng reaver ettercap-graphical
   5:- python3 wifi-tool.py

   
