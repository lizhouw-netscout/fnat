import pexpect
class Gateway:
    def __init__(self):
        self.ipAddress = '192.168.100.1'
        self.username = 'fnet'
        self.password = '1qaz@WSX'
    def set_firewall_disable(self):
        child = pexpect.spawn('ssh %s@%s' % ('fnet',self.ipAddress))
        child.sendline('yes')
        index=child.expect("fnet")
        if ( index == 0 ):
            child.sendline(self.password)
            child.expect('$')
            child.sendline('sudo -k')
            child.sendline('sudo -s')
            child.expect('password for fnet:')
            child.sendline(self.password)
            child.expect('#')
            child.sendline('ufw disable')
            child.sendline('exit')
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

    def set_firewall_enable(self):
        child = pexpect.spawn('ssh %s@%s' % ('fnet',self.ipAddress))
        child.sendline('yes')
        index=child.expect("fnet")
        if ( index == 0 ):
            child.sendline(self.password)
            child.expect('$')
            child.sendline('sudo -k')
            child.sendline('sudo -s')
            child.expect('password for fnet:')
            child.sendline(self.password)
            child.expect('#')
            child.sendline('ufw enable')
            child.sendline('y')
            child.sendline('exit')
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

