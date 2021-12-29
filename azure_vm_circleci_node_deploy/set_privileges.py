from subprocess import Popen, run, PIPE
from waiting import wait

# def myapp_ready():
#     stdout = Popen(['ls'], stdout=PIPE).communicate()

#     output = stdout[0].decode('utf-8')
#     list = output.split('\n')

#     if 'myapp' in list:
#         return True

#     return False

# print('before the wait')

# wait(lambda: myapp_ready(), timeout_seconds=180, waiting_for='creation of myapp')

# print('after the wait')

# stdout = Popen(['ls'], stdout=PIPE).communicate()

# output = stdout[0].decode('utf-8')
# list = output.split('\n')

# if 'myapp' in list:
#     print(True)

def myapp_ready(host):
    print('Waiting for myapp dir to clone in vm')

    stdout, stderr = Popen(['ssh', host, 'ls'], stdout=PIPE).communicate()

    output_str = stdout.decode('utf-8')
    list = output_str.split('\n')

    if 'myapp' in list:
        return True

    return False


def main(PUBLIC_IP):
    host = ''.join(('azureuser@', PUBLIC_IP))
    
    wait(lambda: myapp_ready(host), timeout_seconds=180, sleep_seconds=10, waiting_for='myapp to be created')

    run(['ssh', host, 'sudo', 'usermod', '-g', 'root', 'azureuser'])
    run(['ssh', host, 'sudo', 'chown', '-R', 'azureuser:root', 'myapp'])
    run(['ssh', host, 'sudo', 'chmod', '-R', '770', 'myapp'])

    # stdout, stderr = Popen(['ssh', host, 'ls', '-la', 'myapp'], stdout=PIPE).communicate()

    # output = stdout.decode('utf-8')

    # print(output)