# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:52:48 2022

@author: jacek.kwiecien
"""

menu = '''
Choose what you want to know about me:
1 - My name
2 - My Age
3 - My smile
---------------
To stop this script select 0
'''
smile = '''
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         
                o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       
               o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       
              o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    
             $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$
            $$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$ 
           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     
          o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$
          $$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$
           $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$
            $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
             $$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$
                "$$$$o                            o$$$$
                  "$$$$$oo                      o$$$$
                     ""$$$$$oooo000"$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """""""""""""  
'''

while True:
    print(menu)
    letter = input('Enter your choice:')
    if letter == '1':
        print('My name is Jacek')
        input('Press ENTER to continue')
        continue
    if letter =='2':
        print('I am 37')
        input('Press ENTER to continue')
        continue
    if letter == '3':
        print(smile)
        input('Press ENTER to continue')
        continue
    if letter == '0':
        break

    input("You need to make a valid choice. Press ENTER and try again!")