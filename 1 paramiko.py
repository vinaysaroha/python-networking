import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# allow agent = False means we are not using putty of ssh software
# looks for key = False means we are not using pub.key file to login to any server
ssh_client.connect(hostname='192.168.0.100',port=22,username='root',password='redhat',look_for_keys=False,allow_agent=False)
print('connecting to server...')
print(ssh_client.get_transport().is_active())
print('closing connection...')
ssh_client.close()