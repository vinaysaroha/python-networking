import os
hostname = '192.168.0.100'
response = os.system(f"ping {hostname} -n 1")
print(response)