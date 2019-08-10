#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, os
from core.colors import green, white, red, yellow, end
def logo():
  print """%s
  ██████╗ ███████╗██╗  ██╗ █████╗ ████████╗ ██████╗ 
  ██╔══██╗██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔═══██╗
  ██████╔╝█████╗  ███████║███████║   ██║   ██║   ██║
  ██╔══██╗██╔══╝  ██╔══██║██╔══██║   ██║   ██║   ██║
  ██║  ██║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
  %s
  \t%s*Hacking tools compilation*%s  
  \t%sBy:%s%s mr.z3r0%s                                                                                  
  """%(green, end, red, end, yellow,end,green,end)
  
def menu():
   print """
   [01] Exploits
   [02] DDoS
   [03] Web hacking
   [04] Brute force
   [05] Others
   [99] exit
   """
 
