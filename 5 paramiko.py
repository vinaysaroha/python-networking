import paramiko
import os
import time


command = input("Enter command : ")


def deviation_detail():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    server_list = []
    active_server = []
    not_active_server = []
    # user_name = input("Enter User Name : ")
    # password = input("Enter password: ")
    with open(file="server_ip.txt", mode='r') as server_file:
        for server_ip in server_file:
            server_ip = server_ip.strip()
            server_list.append(server_ip)
    for ip in server_list:
        response = os.system(f"ping {ip} -n 1")
        if response == 0:
            active_server.append(ip)
        else:
            not_active_server.append(ip)
    for server_ip in active_server:
        ssh_client.connect(hostname=server_ip, username="root", password="redhat", port=22, allow_agent=False,
                           look_for_keys=False)
        shell = ssh_client.invoke_shell()
        # if man_page.lower() == 'y':
        #     shell.send('terminal length 0\n')
        time.sleep(0.25)
        shell.send('sudo -i \n')
        time.sleep(0.20)
        shell.send(command + '\n')
        time.sleep(0.5)
        output = shell.recv(1000000).decode()
        with open(file="deviation detail.txt", mode='a') as file:
            file.write(f'{server_ip}\n\n')
            file.write(f'{output}\n\n\n')

        ssh_client.close()
        print("connection closed !!!\n\n\n")
    print(f"Non Active servers are : {not_active_server}")


deviation_detail()
