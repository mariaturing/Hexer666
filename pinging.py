import subprocess

p=subprocess.Popen("ping 8.8.8.8",3)
p.wait()
p.poll()