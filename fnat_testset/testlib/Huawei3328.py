import pexpect

class Huawei3328:
    
    def __init__(self,str_host,str_user=None,str_passwd=None):
        self.ipaddr=str_host
        print('Huawei3328')

    def set_speed_duplex_value(self,port,speed,duplex):
        if (speed == 'auto' and duplex == 'auto'):
            child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
            index=child.expect("<Quidway>")
            if ( index == 0 ):
                child.sendline('system-view')
                child.sendline('int Ethernet %s' % port)
                child.expect('Ether')
                child.sendline('negotiation auto')
                child.sendline('quit')
                child.sendline('quit')
                child.sendline('quit')
            else:
                print ("telnet login failed, due to TIMEOUT or EOF")
                child.close(force=True)
        else:
            child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
            index=child.expect("<Quidway>")
            if ( index == 0 ):
                child.sendline('system-view')
                child.sendline('int Ethernet %s' % port)
                child.expect('Ether')
                child.sendline('undo negotiation auto')
                child.sendline('speed %s' % speed)
                child.sendline('duplex %s' % duplex)
                child.sendline('quit')
                child.sendline('quit')
                child.sendline('quit')
            else:
                print ("telnet login failed, due to TIMEOUT or EOF")
                child.close(force=True)


    def set_poe_enable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
        index=child.expect("<Quidway>")  
        if ( index == 0 ):
            child.sendline('system-view')
            child.sendline('int Ethernet %s' % port)
            child.expect('Ether')
            child.sendline('poe enable')
            child.sendline('quit')
            child.sendline('quit')
            child.sendline('quit')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)

    def set_poe_disable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
        index=child.expect("<Quidway>")  
        if ( index == 0 ):
            child.sendline('system-view')
            child.sendline('int Ethernet %s' % port)
            child.expect('Ether')
            child.sendline('undo poe enable')
            child.sendline('quit')
            child.sendline('quit')
            child.sendline('quit')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)

    def set_lldp_enable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
        index=child.expect("<Quidway>")  
        if ( index == 0 ):
            child.sendline('system-view')
            child.sendline('int Ethernet %s' % port)
            child.expect('Ether')
            child.sendline('lldp enable')
            child.sendline('quit')
            child.sendline('quit')
            child.sendline('quit')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)

    def set_lldp_disable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
        index=child.expect("<Quidway>")  
        if ( index == 0 ):
            child.sendline('system-view')
            child.sendline('int Ethernet %s' % port)
            child.expect('Ether')
            child.sendline('undo lldp enable')
            child.sendline('quit')
            child.sendline('quit')
            child.sendline('quit')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)


