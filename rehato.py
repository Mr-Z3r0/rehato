#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys, time, subprocess
from core.colors import green, white, red, yellow, end
from core.menu import *
from core.recore import *
def mp():
 menu()
 while True:
  op = raw_input("%sChoose>> %s"%(red,end))
  if op == "1" or op =="01":
   print """
   [01] Metasploit
   [02] sqlmap
   [03] RouterSploit
   [04] A-Rat
   [05] Websploit
   [06] WPSploit
   [99] Back to main menu\n
   """
   sq = raw_input("%sChoose>> %s"%(red,end))
   if sq == "1" or sq == "01":
    metasploit()
   elif sq == "2" or sq == "02":
    sqlmap()
   elif sq == "3" or sq == "03":
     routersploit()
   elif sq == "4" or sq == "04":
     a_rat()
   elif sq == "5" or sq == "05":
     websploit()
   elif sq == "6" or sq == "06":
    WPSploit()
   elif sq == "99": 
    program_restart() 
   else:
     print "\nERROR: Wrong Input"
     time.sleep(2)
     program_restart()
  elif op == "2" or op == "02":
    print """
    [01] Bigf0x
    [02] Slowloris
    [03] Torshammer
    [04] Xerxes
    [05] Planetwork-DDOS
    [06] Fl00d & Fl00d2
    [99] Back to main menu\n
    """
    sq1 = raw_input("%sChoose>> %s"%(red,end))
    if sq1 == "1" or sq1 == "01":
     bigf0x()
    elif sq1 == "2" or sq1 == "02":
     slowloris()
    elif sq1 == "3" or sq1 == "03":
     torshammer()
    elif sq1 == "4" or sq1 == "04":
     xerxes()
    elif sq1 == "5" or sq1 == "05":
     Planetwork-DDOS()
    elif sq1 == "6" or sq1 == "06":
     fl00dfl00d2()
    elif sq1 == "99": 
     program_restart() 
    else:
     print "\nERROR: Wrong Input"
     time.sleep(2)
     program_restart()
  elif op =="3" or op == "03":
   print """
   [01] Sqlmap
   [02] SqlDump
   [03] Xshell
   [04] Vulnz
   [05] Websploit
   [06] Ko-Dork
   [07] Webdav
   [99] Back to main menu\n
   """
   sq2 = raw_input("%sChoose>> %s"%(red,end))
   if sq2 == "1" or sq2 == "01":
    sqlmap()
   elif sq2 == "2" or sq2 == "02":
    sqldump()
   elif sq2 == "3" or sq2 == "03":
    Xshell
   elif sq2 == "4" or sq2 == "04":
    Vulnz()
   elif sq2 == "5" or sq2 == "05":
    Websploit()
   elif sq2 == "6" or sq2 == "06":
    kodork()
   elif sq2 == "7" or sq2 == "07":
    webdav()
   elif sq2 == "99":
    program_restart()
   else: 
    print "[!] Wrong command"
    time. sleep(2)
    program_restart()
  elif op == "4" or op == "04":
   print """
    [01] Cupp
    [02] Hydra
    [03] FBBRUTE
    [04] InstaHack
    [05] Black Hydra
    [06] Crunch
    [07] Social-Engineering
    [08] Facebook Brute Force 3
    [99] Back to main menu\n
   """
   sq3 = raw_input("%sChoose>> %s"%(red,end))
   if sq3 == "1" or sq3 == "01":
    cupp()
   elif sq3 == "2" or sq3 == "02":
    hydra()
   elif sq3 == "3" or sq3 == "03":
    fbbrute()
   elif sq3 == "4" or sq3 == "04":
    instahack()
   elif sq3 == "5" or sq3 == "05":
    blackhydra()
   elif sq3 == "6" or sq3 == "06":
    crunch()
   elif sq3 == "7" or sq3 == "07":
    socialengineering()
   elif sq3 == "8" or sq3 == "08":
    fbbrute3()
   elif sq3 == "99":
    program_restart()
   else:
    print "[!] wrong command!"
    time. sleep(2)
    program_restart()
  elif op =="5" or op == "05":
   print """
    [01] Ngrok
    [02] Nano
    [03] Kali Nethunter
    [04] Termux-Styling
    [05] Ubuntu
    [06] Fedora
    [07] SpotifyChecker
    [08] Passgen
    [99] Back to main menu\n
   """
   sq4 = raw_input("%sChoose>> %s"%(red,end))
   if sq4 == "1" or sq4 == "01":
    ngrok()
   elif sq4 == "2" or sq4 == "02":
    Nano()
   elif sq4 == "3" or sq4 == "03":
    kalinethunter()
   elif sq4 == "4" or sq4 == "04":
    termux_styling()
   elif sq4 == "5" or sq4 == "05":
    ubuntu()
   elif sq4 == "6" or sq4 == "06":
    fedora()
   elif sq4 == "7" or sq4 == "07":
    spotifychecker()
   elif sq4 == "8" or sq4 == "08":
    passgen()
   elif sq4 == "99":
    program_restart()
   else: 
    print "[!] wrong command!"
    time. sleep(2)
    program_restart()
  elif op == "99" or op == "exit":
   sys.exit()
  else:
   print "[!] wrong command!"
   time. sleep(2)
   program_restart()
def control():
    try:
        logo()
        mp()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected, Exiting. . .")
        time.sleep(2)
        sys.exit()
        
if __name__ == "__main__":
 control()
