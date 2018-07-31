import pexpect

class HP2910:
    
    def __init__(self,str_host,str_user=None,str_passwd=None):
        self.ipaddress=str_host
    def set_speed_duplex_value(self,port,speed,duplex):
        child = pexpect.spawn('telnet %s' % self.ipaddress,timeout=30)
        child.sendline('c')
        index=child.expect("#")  
        if ( index == 0 ):
            child.sendline('conf t')
            child.expect('config')
            child.sendline('int ethernet %s' % port)
            child.expect('eth-')
            child.sendline('speed-duplex %s' % speed)
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('y')
            print('Function set_speed_duplex_value is ok')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)
            


    def set_poe_enable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddress,timeout=30)
        child.sendline('c')
        index=child.expect("#")  
        if ( index == 0 ):
            child.sendline('conf t')
            child.expect('config')
            child.sendline('int %s power-over-ethernet' % port )
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('y')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)
    def set_poe_disable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddress,timeout=30)
        child.sendline('c')
        index=child.expect("#")  
        if ( index == 0 ):
            child.sendline('conf t')
            child.expect('config')
            child.sendline('no int %s power-over-ethernet' % port )
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('y')
        else:
            print ("telnet login failed, due to TIMEOUT or EOF")
            child.close(force=True)

    def set_lldp_enable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddress,timeout=30)
        child.sendline('c')
        index=child.expect("#")  
        if ( index == 0 ):
            child.sendline('conf t')
            child.expect('config')
            child.sendline('no int %s power-over-ethernet' % port )
            child.sendline('lldp run')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('y')
        else:    
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)

    def set_lldp_disable(self,port):
        child = pexpect.spawn('telnet %s' % self.ipaddress,timeout=30)
        child.sendline('c')
        index=child.expect("#")  
        if ( index == 0 ):
            child.sendline('conf t')
            child.expect('config')
            child.sendline('no int %s power-over-ethernet' % port )
            child.sendline('no lldp run')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('exit')
            child.sendline('y')
        else:    
            print ("telnet login failed, due to TIMEOUT or EOF") 
            child.close(force=True)


