#Simple Pinger
#by Tom Knudsen

import subprocess
import os

#This program invokes a for loop to ping a range between 1-256
with open(os.devnull, "wb") as limbo:
        for n in range(1, 256):
                ip="192.168.10.{0}".format(n) #This defines the ip to be pinged 
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                #this checks to see if the host is active
                if result:
                        print(ip, "inactive")
                else:
                        print(ip, "active")
