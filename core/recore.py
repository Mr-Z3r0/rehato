import sys, os, time
from core.colors import *
def program_restart():
   python = sys.executable
   os.execl(sys.executable, sys.executable, *sys.argv)
   curdir = os.getcwd()
def b_menu():
 print """
 [99] Back  to main menu
 [00] Exit
 """
def backtomenu_option():
	b_menu()
	backtomenu = raw_input("lzmx > ")
	
	if backtomenu == "99":
		program_restart()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		program_restart()

def metasploit():
  print '\n%sInstalling Metasploit%s'%(red,end)
  os.system("apt update && apt upgrade")
  os.system("apt install git wget curl")
  os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
  os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
  print """
  ###### Done
  ###### Type 'msfconsole' to start."""
  backtomenu_option()
def sqlmap():
 print '\n%sInstalling Sqlmap%s'%(green,end)
 os.system("apt update && apt upgrade")
 os.system("pip2 install sqlmap")
 print """
 #### Done
 #### Type sqlmap to start.
 """
 backtomenu_option()
def routersploit():
 print '\n%sInstalling routersploit%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('python2 -m pip install requests')
 os.system('git clone https://github.com/reverse-shell/routersploit')
 os.system('mv routersploit ~;cd ~/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py')
 print '#### Done'
 backtomenu_option()
def a_rat():
 print '\n%s#### Installing A-Rat%s'%(green, end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('git clone https://github.com/Xi4u7/A-Rat')
 os.system('mv A-Rat ~')
 print '###### Done'
 backtomenu_option()
def websploit():
 print '\n%s#### Installing Websploit%s'%(green, end)
 os.system('apt update && apt upgrade')
 os.system('apt install git python2')
 os.system('python2 -m pip install scapy')
 os.system('git clone https://github.com/The404Hacking/websploit')
 os.system('mv websploit ~')
 print '###### Done'
 backtomenu_option()
 backtomenu_option()
def WPSploit():
 print '\n%s###### Installing WPSploit%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('git clone https://github.com/m4ll0k/wpsploit')
 os.system('mv wpsploit ~')
 print '###### Done'
 backtomenu_option()
def bigf0x():
 print '\n%s###### Installing bigf0x%s'%(green,end)
 os.system("apt update && apt upgtade")
 os.system("apt install python2 git")
 os.system("git clone https://github.com/mr-z3r0/bigf0x")
 os.system("mv bigf0x ~")
 print "#### Done :D"
 backtomenu_option()
def slowloris():
 print '\n%s###### Installing SlowLoris%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('git clone https://github.com/gkbrk/slowloris')
 os.system('mv slowloris ~')
 print "#### Done"
 backtomenu_option()
 
def torshammer():
 print '\n%s###### Installing torshammer%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('git clone https://github.com/dotfighter/torshammer')
 os.system('mv torshammer ~')
 print '###### Done'
 backtomenu_option()
def xerxes():
 print '\n%s###### Installing Xerxes%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git')
 os.system('apt install clang')
 os.system('git clone https://github.com/zanyarjamal/xerxes')
 os.system('mv xerxes ~')
 os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
 print '###### Done'
 backmenu_option()
def Planetwork_DDOS():
 print '\n%s###### Installing Planetwork DDoS%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git python2')
 os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
 os.system('mv Planetwork-DDOS ~')
 print '###### Done'
 backtomenu_option()
def fl00dfl00d2():
  print '\n%s###### Installing Fl00d & Fl00d2%s'%(green,end)
  os.system('apt update && apt upgrade')
  os.system('apt install python2 curl')
  os.system('mkdir ~/fl00d')
  os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
  os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
  os.system('mv fl00d.py ~/fl00d && mv fl00d2.py ~/fl00d')
  print '###### Done'
  backtomenu_option()
def sqldump():
 print '\n%s###### Installing Fl00d & Fl00d2%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 curl')
 os.system('python2 -m pip install google')
 os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
 os.system('mkdir ~/sqldump && chmod +x sqldump.py && mv sqldump.py ~/sqldump')
 print '###### Done'
 backtomenu_option()
def xshell():
 print '\n%s#### Installing xshell%s'%(green,end)
 os.system("apt update && apt upgrade")
 os.system("apt install lynx python2 figlet ruby php nano w3m")
 os.system("git clone https://github.com/Ubaii/Xshell")
 os.system("mv Xshell ~")
 print '###### Done'
 backtomenu_option()
def vulnz():
 print '\n%s#### Installing vulnz%s'%(green,end)
 os.system("apt update && apt upgrade")
 os.system('apt install python2 git')
 os.system('git clone https://github.com/mr-z3r0/vulnz')
 os.system('mv Vulnz ~')
 print "#### Done"
 backtomenu_option()
def kodork():
 print '\n%s#### Installing Ko-Dork%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git python2 && python2 -m pip install urllib2')
 os.system('git clone https://github.com/ciku370/ko-dork')
 os.system('mv ko-dork ~')
 print '###### Done'
 backtomenu_option()
def webdav():
 print '\n%s#### Installing webdav%s'%(green,end)
 os.system("apt update && apt upgrade")
 os.system("apt install python2 openssl curl libcurl")
 os.system("python2 -m pip install requests")
 os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
 os.system("mkdir ~/webdav-mass-exploit && mv webdav.py ~/webdav-mass-exploit")
 print '###### Done'
 backtomenu_option()
def ngrok():
 print '\n%s#### Installing Ngrok%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git')
 os.system('git clone https://github.com/themastersunil/ngrok')
 os.system('mv ngrok ~')
 print '###### Done'
 backtomenu_option()
def Nano():
 print '\n%s#### Installing Nano%s'%(green,end)
 os.system("apt update && aot upgrade")
 os.system("pkg install nano")
 print """
 #### Done
 #### Type nano to start
 """
def kalinethunter():
 print '\n%s#### Installing Kali Nethunter%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git')
 os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
 os.system('mv Nethunter-In-Termux ~')
 print '###### Done'
 backtomenu_option()
 
def ubuntu():
 print '\n%s#### Installing ubuntu%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install python2 git')
 os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
 os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
 print '###### Done'
 backtomenu_option()
def fedora():
 print '\n%s#### Installing fedora%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install wget git')
 os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
 os.system('mv termux-fedora.sh ~')
 print '###### Done'
 backtomenu_option()
def spotifychecker():
 print '\n%s#### Installing spotify checker%s'%(green,end)
 os.system("apt update && apt upgrade")
 os.system("apt install git php")
 os.system("git clone https://github.com/mr.z3r0/spotibrute")
 os.system("mv spotibrute ~")
 print "#### Done"
 backtomenu_option()
def passgen():
 print '\n%s#### Installing passgen%s'%(green,end)
 os.system('apt update && apt upgrade')
 os.system('apt install git php')
 os.system('git clone https://github.com/Cvar1984/PassGen')
 os.system('mv PassGen ~')
 print '###### Done'
 backtomenu_option()
 
