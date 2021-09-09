import paramiko
import time
import os



ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
user_name = input("Enter username: ")
password = input("Enter password: ")
command = input("Enter the command: ")
# man_page = input("Do you need to read man page y/n: ")
try:

    server_list = []
    with open(file="server_ip.txt", mode='r') as server_file:
        for server_ip in server_file:
            ip = server_ip.strip()
            server_list.append(ip)
    for server_ip in server_list:
        ssh_client.connect(hostname=server_ip, username=user_name, password=password, port=22, allow_agent=False,
                           look_for_keys=False)
        print(f"Connected to {server_ip}")
        shell = ssh_client.invoke_shell()
        # if man_page.lower() == 'y':
        #     shell.send('terminal length 0\n')
        shell.send(command + '\n')
        time.sleep(1)
        output = shell.recv(1000000).decode()
        # output = output.decode('utf-8')
        with open(file="deviation detail.txt", mode='w') as file:
            file.write(output)
        ssh_client.close()
        print("connection closed !!!\n\n\n")

except Exception as ex:
    print(ex)
