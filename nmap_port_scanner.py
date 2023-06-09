#!/usr/bin/env python3

import nmap
import ipaddress  #Importing for IP address validation
import re  #Importing module for regular expressions

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")  #Regular expression pattern for extracting port range
port_min = 0  #Initializing minimum port number
port_max = 65535  #Initializing maximum port number

while True:
    ip_add_entered = input("\nPlease enter the IP address you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)  #Validating the entered IP address
        print("You entered a valid IP address.")
        break
    except:
        print("You entered an invalid IP address")

#This scanner is basic so scanning all the ports is not advised.
while True:
    print("Please enter the range of ports you want to scan in the format: <int>-<int> (e.g., 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))  #Removing extra spaces from the input
    if port_range_valid:
        port_min = int(port_range_valid.group(1))  #Extracting the lower end of the port range
        port_max = int(port_range_valid.group(2))  #Extracting the upper end of the port range
        break

nm = nmap.PortScanner()  #Creating a new nmap PortScanner instance

for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))  #Scanning the specified port on the IP address
        port_status = result['scan'][ip_add_entered]['tcp'][port]['state']  #Extracting the port status from the result
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")
