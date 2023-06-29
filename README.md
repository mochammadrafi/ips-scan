# IPs Scanner

This Python script allows you to scan a list of IP addresses and check the status of specific ports. It utilizes the socket module to establish a TCP connection with each IP address and port combination provided.
### Features
- Scans a list of IP addresses and checks the status of specified
- Saves the IP address and open ports to a file for further analysis

### Prerequisites
- Python 3.x
- ips.txt file: Contains a list of IP addresses, with each IP address on a separate line.

### Usage
1. Ensure that you have the ips.txt file in the same directory as the script.
2. Modify the ports list variable to include the ports you want to check.
3. Run the script using the command python port_scanner.py.
4. The script will iterate over each IP address and port combination, attempting to establish a connection.
5. If a connection is successful, the script will print that the IP address and port are open and save the information to open_ports.txt.
6. If a connection is unsuccessful, the script will print that the IP address and port are closed.
7. After the scan is complete, you can open open_ports.txt to view the IP addresses and open ports found.

**Note**: Please exercise caution and ensure that you have proper authorization before scanning any IP addresses or ports.
License

This project is licensed under the [MIT License](https://github.com/mochammadrafi/ips-scan/blob/main/LICENSE).
