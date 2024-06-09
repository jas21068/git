


import os
import paramiko
import time
# os.chdir('C:/')
# f = open('fortigate.conf','r')
# print(f.read(5))
# print(f.tell())
# print(f.seek(1))
# print(f.read(5))
#
# f.closed

# with open('fortigate.conf') as file:
#     content = file.read()
#     print(content)
#
# with open('fortigate.conf') as file:
#     content = file.read().split()
#
#     # print(content)
#     b=len(content)
#     print(len(content))
#
#     for i in range(b):
#         if content[i] == 'ip':
#             print(''+ content[i+1] + '  ' + content[i+2])
#

while True:
    ssh_client = paramiko.SSHClient()
    print(type(ssh_client))

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip = '172.16.1.1'
    port = '80'
    user = 'admin'
    pwd = 'admin'
    ips = ['diag debug en', 'diagnose ips memory status', 'diagnose ips session status', 'diagnose ips packet status',
           'get sys perf stat', 'diag ips session list']
    router = {'hostname': ip, 'port': port, 'username': user, 'password': pwd}
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    # creating a shell object
    shell = ssh_client.invoke_shell()
    time.sleep(4)
    # sending commads to the remote device to execute them
    # each command ends  in \n (new line, the enter key)
    for i in ips:
        print(i)
        shell.send(i + '\n')
    shell.send('get system status\n')
    shell.send('get system performance status\n')
    shell.send('get router info routing-table all\n')
    shell.send('di sys top 2 20\n')
    time.sleep(10)  # waiting for the remove device to finish executing the commands (mandatory)

    # reading from the shell's output buffer
    output = shell.recv(10000000)
    print(output)
    # print(type(output))
    output = output.decode('utf-8')  # decoding from bytes to string
    print(output)

    # closing the connection if it's active
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()














