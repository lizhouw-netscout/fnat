import pexpect
import time
class Juniper2200:
   

  def __init__(self,str_host,str_user,str_passwd):
      self.ipaddr=str_host
      self.username=str_user
      self.passwd=str_passwd
      print('Juniper2200')

  def set_speed_duplex_value(self,port,speed,duplex):
      if (duplex == 'auto'):
         child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
         index=child.expect("login:")
         if( index == 0 ):
             child.sendline(self.username)
             child.expect('Password:')
             child.sendline(self.passwd)
             child.expect('>')
             child.sendline('configure')
             child.expect('#')
             child.sendline('set int %s ether-options auto-negotiation speed %s' % (port,speed))
             child.sendline('commit')
             time.sleep(5)
             child.sendline('exit')
             time.sleep(2)
             child.sendline('exit')
         else:
             print ("telnet login failed, due to TIMEOUT or EOF")
             child.close(force=True)

      else:
          child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
          index=child.expect("login:")
          if ( index == 0 ):
              child.sendline(self.username)
              child.expect('Password:')
              child.sendline(self.passwd)
              child.expect('>')
              child.sendline('configure')
              child.expect('#')
              child.sendline('set int %s ether-options no-auto-negotiation' % port)
              child.sendline('set int %s ether-options speed %s' % (port,speed))
              child.sendline('set int %s ether-options link-mode %s' % (port,duplex))
              child.sendline('commit')
              time.sleep(5)
              child.sendline('quit')
              time.sleep(2)
              child.sendline('quit')
          else:
              print ("telnet login failed, due to TIMEOUT or EOF")
              child.close(force=True)

  def set_poe_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("login:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('configure')
          child.expect('#')
          child.sendline('set poe interface %s disable' % port)
          child.sendline('delete poe interface %s disable' % port)
          child.sendline('commit')
          time.sleep(5)
          child.sendline('exit')
          time.sleep(2)
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)

  def set_poe_disable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("login:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('configure')
          child.expect('#')
          child.sendline('set poe interface %s disable' % port)
          child.sendline('commit')
          time.sleep(5)
          child.sendline('exit')
          time.sleep(2)
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)

  def set_lldp_disable(self,port):
     child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
     index=child.expect("login:")
     if ( index == 0 ):
         child.sendline(self.username)
         child.expect('Password:')
         child.sendline(self.passwd)
         child.expect('>')
         child.sendline('configure')
         child.expect('#')
         child.sendline('set protocols lldp int %s disable' % port)
         child.sendline('set protocols lldp-med int %s disable' % port)
         child.sendline('commit')
         time.sleep(5)
         child.sendline('exit')
         time.sleep(2)
         child.sendline('exit')
     else:
         print ("telnet login failed, due to TIMEOUT or EOF")
         child.close(force=True)

  def set_lldp_enable(self,port):
      child = pexpect.spawn('telnet %s' % self.ipaddr,timeout=30)
      index=child.expect("login:")
      if ( index == 0 ):
          child.sendline(self.username)
          child.expect('Password:')
          child.sendline(self.passwd)
          child.expect('>')
          child.sendline('configure')
          child.expect('#')
          child.sendline('set protocols lldp int %s disable' % port )
          child.sendline('set protocols lldp-med int %s disable' % port)
          child.sendline('delete protocols lldp-med int %s disable' % port)
          child.sendline('delete protocols lldp int %s disable' % port)
          child.sendline('commit')
          time.sleep(5)
          child.sendline('exit')
          time.sleep(2)
          child.sendline('exit')
      else:
          print ("telnet login failed, due to TIMEOUT or EOF")
          child.close(force=True)





