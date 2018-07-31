import pexpect

class Cisco3560:
   

  def __init__(self,str_host,str_user,str_passwd):
      self.ipaddr=str_host
      self.username=str_user
      self.passwd=str_passwd
      self.administrator = '123'
      print('Cisco3560')

  def set_speed_duplex_value(self,port,speed,duplex):
        ##speed:10,100,1000,auto##
        ##duplex:auto,full,half##
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('int giga %s' % port)
          child.expect('if')
          child.sendline('speed %s' % speed)
          child.sendline('duplex %s' % duplex)
          child.sendline('exit')
          child.sendline('exit')
          child.sendline('exit')
     
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)


  def set_poe_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('int giga %s' % port)
          child.expect('if')
          child.sendline('power inline auto')
          child.sendline('exit')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)
  def set_poe_disable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('int giga %s' % port)
          child.expect('if')
          child.sendline('power inline never')
          child.sendline('exit')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)

  def set_lldp_disable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('no lldp run')
          child.sendline('no cdp run')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)

  def set_lldp_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('lldp run')
          child.sendline('no cdp run')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)


  def set_cdp_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('no lldp run')
          child.sendline('cdp run')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)

  def set_lldp_cdp_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("Username:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('enable')
          child.expect('Password:')
          child.sendline(self.administrator)
          child.expect('#')
          child.sendline('conf t')
          child.expect('config')
          child.sendline('lldp run')
          child.sendline('cdp run')
          child.sendline('exit')
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)
   
   
