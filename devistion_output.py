import paramiko
import time
import os


command = input("Enter command: ")
def deviation_detail():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    active_server = []
    not_active_server = []
    user_name = input("Enter User Name : ")
    password = input("Enter password")
    with open(file="server_ip.txt", mode='r') as server_file:
        for server_ip in server_file:
            server_ip = server_ip.strip()
            active_server.append(server_ip)
    for ip in active_server:
        response = os.system(f"ping {ip} -n 1")
        if response == 0:
            active_server.append(ip)
        else:
            not_active_server.append(ip)
    for server in active_server:
        ssh_client.connect(hostname=server_ip, username=user_name, password=password, port=22, allow_agent=False,
                           look_for_keys=False)
        print(f"Connected to {server}")
        shell = ssh_client.invoke_shell()
        # if man_page.lower() == 'y':
        #     shell.send('terminal length 0\n')
        shell.send(command + '\n')
        time.sleep(1)
        output = shell.recv(1000000).decode()
        with open(file="deviation detail.txt", mode='w') as file:
            file.write(output)
        ssh_client.close()
        print("connection closed !!!\n\n\n")
    print(f"Non Active servers are : {not_active_server}")
