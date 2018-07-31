import pexpect
class Nistnet:
    def __init__(self):
        self.ipAddress = '192.168.1.30'
        self.username = 'root'
        self.password = '1qaz@WSX'
    def set_nistnet_value(self,A,B,C,D,E,F):
        child = pexpect.spawn('ssh %s@%s' % ('root',self.ipAddress))
        child.sendline('yes')
        index=child.expect("root")
        if ( index == 0 ):
            child.sendline(self.password)
            child.expect('#')
            child.sendline('cd /home/nistnet.2.0.12b')
            child.expect('nistnet.2.0.12b')
            child.sendline('./Load.Nistnet')
            child.sendline('cnistnet -u')
            child.sendline('cnistnet -a %s %s --delay %s --drop %s --dup %s --bandwidth %s' % (A,B,C,D,E,F))
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

    def del_nistnet_value(self,A,B,C,D,E,F):
        child = pexpect.spawn('ssh %s@%s' % ('root',self.ipAddress))
        child.sendline('yes')
        index=child.expect("root")
        if ( index == 0 ):
            child.sendline(self.password)
            child.expect('#')
            child.sendline('cd /home/nistnet.2.0.12b')
            child.expect('nistnet.2.0.12b')
            child.sendline('./Load.Nistnet')
            child.sendline('cnistnet -u')
            child.sendline('cnistnet -r %s %s --delay %s --drop %s --dup %s --bandwidth %s' % (A,B,C,D,E,F))
            child.sendline('exit')
            child.close()
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

