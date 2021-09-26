import paramiko
import os
import time
import csv

command = input("Enter command : ")

def deviation_detail():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    server_list = []
    active_server = []
    not_active_server = []
    password_not_working = []
    email_id = []
    # user_name = input("Enter User Name : ")
    # password = input("Enter password: ")
    with open("C:\\Users\\vsaroha\\Documents\\data.csv") as f:
        all_server_data = list(csv.reader(f))
        print(all_server_data)
        for server_data in all_server_data:
            server_list.append(server_data[0])
    for ip in server_list:
        response = os.system(f"ping {ip} -n 1")
        if response == 0:
            active_server.append(ip)
        else:
            not_active_server.append(ip)
    print(f"{active_server} is active servers")
    print(f"{email_id} is the email id")
    print(f"{not_active_server} is non active servers")
    for server_ip in active_server:
        try:
            if ssh_client.connect(hostname=server_ip, username="root", password="redhat", port=22, allow_agent=False,
                                  look_for_keys=False) is None:

                ssh_client.connect(hostname=server_ip, username="root", password="redhat", port=22, allow_agent=False,
                                   look_for_keys=False)
                print()
                print(f"connection open for {server_ip}")
                shell = ssh_client.invoke_shell()
                # if man_page.lower() == 'y':
                #     shell.send('terminal length 0\n')
                time.sleep(0.25)
                shell.send('sudo -i \n')
                time.sleep(0.20)
                shell.send(command + '\n')
                time.sleep(0.5)
                for every_server_list in all_server_data:
                    if every_server_list[0].lower() == server_ip.lower():
                        email_id.append(every_server_list[2])
                        output = shell.recv(1000000).decode()
                        with open(file=f"{every_server_list[2]}.txt", mode='a') as file:
                            file.write(f"{output}\n\n\n")

                # with open(file="deviation detail.txt", mode='a') as file:
                #     file.write(f'{server_ip}\n\n')
                #     file.write(f'{output}\n\n\n')

                ssh_client.close()
                print(f"connection closed {server_ip}!!!\n\n\n")
        except Exception as ex:
            password_not_working.append(server_ip)
            print(f'Server is pingable but not able to connect {server_ip}\nreason is:\n{ex}')
            print()
            continue
    print(all_server_data)


if __name__ == '__main__':
    deviation_detail()
