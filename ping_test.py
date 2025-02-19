#!/usr/bin/env python3

import subprocess
import socket 
import os

os.system('clear')

print("")
print("")
print("Script written by: Mina Ramez Farag")
print("")
print("       **************************************")
print("       *******PING TEST TROUBLESHOOTER*******")
print("       **************************************")
print("")
print("Enter Selection:")
print("")
print("       1 - Test connectivity to your gateway.")
print("       2 - Test for remote connectivity.")
print("       3 - Test for DNS resolution.")
print("       4 - Display gateway IP address.")
print("")


#check the gateway connection on port 80
def gateway_connection():
    gateway_address= input("Please enter the gateway address: ")
    gateway_port= 80
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(5)
            result = connection.connect_ex((gateway_address,gateway_port))
            if result == 0:
                print("Successfully connected to the gateway!")
                return True
            else:
                print("Could not connect to the gateway!")
                return False
    except socket.error as error:
        print(f"Socket error: {error}")
        return False




#test for remote connections using the google host network
def remote_connection():
    host= "8.8.8.8"
    port= 443

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout( 5 )

    try:
        sock.connect((host, port))
    except socket.error as e:
        print(f"Connection to {host}:{port} failed: {e}!")
        return False

    print(f"Successfully connected to {host}:{port}!")
    return True




#test for dns resolution using the google host 
def dns_resolution( ):
    hostname= "www.google.com"

    try:
        ip_address= socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"DNS resolution for {hostname} failed: {e}!")
        return False

    print(f"Successfully resolved {hostname} to {ip_address}!")
    return True




#print the gateway for the user
def print_gateway():
    p= subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)
    out =p.stdout.read( ).decode("utf-8")

    lines=  out.split("\n" )

    for line in lines:
        if "default" in line:
            fields = line.split( )
            global gateway_address
            gateway_address = fields[2]
            break
    else:
        print("Default gateway not found!")
        return

    print(f"Default gateway: {gateway_address}!")



def run_code(user_entry):
    if user_entry == 1:
        gateway_connection()

    elif user_entry == 2:
        remote_connection()
        
    elif user_entry == 3:
        dns_resolution()
        
    elif user_entry == 4:
        print_gateway()
        

while True:
    print("")
    user_input = input("Enter a number from 1 - 4, or 'Q/q' to exit: ")
    if user_input.lower() == 'q':
        break
    try:
        user_entry = int(user_input)
        if user_entry >= 1 and user_entry <= 4:
            run_code(user_entry)
        
        else:
            print("please enter a number from 1 - 4.")
    except ValueError:
        print("please enter a number from 1 - 4")