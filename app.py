import socket

def check_web_service(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set timeout for connection attempt

        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip, port))

        # Check if the connection was successful
        if result == 0:
            print(f"IP: {ip} - Port: {port} is open")
            # Save the IP address and port to a file
            with open("open_ports.txt", "a") as f:
                f.write(f"{ip}:{port}\n")
        else:
            print(f"IP: {ip} - Port: {port} is closed")

        sock.close()
    except socket.error as e:
        print(f"Error: {e}")

# List of IP addresses to scan in ips.txt
with open("ips.txt", "r") as f:
    ip_addresses = f.read().splitlines()

# Ports to check (HTTP and HTTPS)
ports = [80, 443, 8080, 8443, 8000, 8008, 8888]

# Iterate over each IP address and port combination
for ip in ip_addresses:
    for port in ports:
        check_web_service(ip, port)
