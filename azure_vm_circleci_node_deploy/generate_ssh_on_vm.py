from subprocess import Popen, run, PIPE

def main(PUBLIC_IP):
    host = ''.join(('azureuser@', PUBLIC_IP))

    run(['ssh', host, 'ssh-keygen'])
    run(['ssh', host, 'cat', './.ssh/id_rsa.pub', '>>', './.ssh/authorized_keys'])
    
    stdout, stderr = Popen(['ssh', host, 'cat', './.ssh/id_rsa'], stdout=PIPE).communicate()

    PRIVATE_KEY = stdout.decode('utf-8')

    return PRIVATE_KEY
