import socket
import subprocess

subprocess.run(["ipconfig","/all"],shell=True)

subprocess.run(["arp", "-a"], shell=True)
