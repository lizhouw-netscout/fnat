import pexpect
class DHCP:
    def __init__(self):
        self.ipAddress = '192.168.100.1'
        self.username = 'fnet'
        self.password = '1qaz@WSX'
    def set_dhcp_start(self):
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
            child.sendline('/etc/init.d/isc-dhcp-server start')
            child.sendline('exit')
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

    def set_dhcp_stop(self):
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
            child.sendline('/etc/init.d/isc-dhcp-server stop')
            child.sendline('exit')
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

