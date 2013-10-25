#!/usr/bin/env python
# -*- coding: utf-8 -*-


nstar = input("Enter the number of stars : ") 


"""
*
**
***
****
"""
cstar = 1
cline = nstar
while cline > 0:
    
    for c in range(0,cstar):
        print "*",
    
    print 
    cstar+=1
    cline-=1


print
"""
****
***
**
*
"""
cline = nstar
while cline > 0:
    
    cstar = 1
    while cstar <= cline:
        print "*",
        cstar += 1
    
    print 
    cline-=1


print

"""
****
 ***
  **
   *
"""
spaces = 0
cline = nstar
cstar = nstar
while cline > 0:
    
    
    for c in range(0,spaces):
        print " ",
        
    for c in range(0,cstar):
        print "*",
    
    print 
    cstar-=1
    spaces+=1
    cline-=1


print

"""
   *
  **
 ***
****
"""

cline = nstar
spaces = nstar - 1
cstar = 1
while cline > 0:
    
    
    for c in range(0,spaces):
        print " ",
        
    for c in range(0,cstar):
        print "*",
    
    print 
    cstar+=1
    spaces-=1
    cline-=1

print


