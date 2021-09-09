import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
        ssh_client.connect(hostname='192.168.0.101', username='root', password='redhat', port=22, allow_agent=False,
                           look_for_keys=False)
        print(f"Connected to server")
        shell = ssh_client.invoke_shell()
        shell.send('cat /root/.ssh/authorized_keys \n')
        shell.send('last|head -n10\n')
        time.sleep(5)
        output = shell.recv(1000000).decode()
        with open("server_output.txt",'w') as file:
                file.write(output)
        ssh_client.close()
        print("connection closed !!!")

except Exception as ex:
    print(ex)
