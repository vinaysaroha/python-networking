import paramiko
import time

command = input("Enter the command :  ")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
server = {'hostname': '192.168.0.100', 'port': 22, 'username': 'root', 'password': 'redhat'}
ssh_client.connect(**server, allow_agent=False, look_for_keys=False)
print(f"connected to {server['hostname']}")
shell = ssh_client.invoke_shell()
read_man = input("Do you want to read page output y/n: ")
if read_man.lower() == 'y':
    shell.send(
        'terminal length 0\n')  # to see the complete page or output as in man page its ask us to press enter or space to read more or go done into the page.
shell.send(f'{command}\n')
time.sleep(1)
output = shell.recv(100000)  # how much byte you want to receive
output = output.decode('utf-8')
print(output)
connection_close = input("Do you want to close the connection y/n: ")
if connection_close.lower() == 'y':
    ssh_client.close()
    print(f"connection closed")
# if (ssh_client.get_transport().is_active() ==True):
#     print('closing connection')
#     ssh_client.close()
