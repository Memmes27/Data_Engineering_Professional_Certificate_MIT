import os
import sys


# -------------
# Input argurments
# -------------
# -list, list files
# -listHidden, list hidden files

# list files
def list_files():
    for item in os.listdir('.'):
        if not item.startswith('.'):
            print(item)

def list_hidden_files():
    for item in os.listdir('.'):
        print(item)

#read input arguments
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]
else:
    argument = ''

#if -list list files
if (argument == '-list'):
    list_files()

#if -list list hiddenfiles
if (argument == '-listhidden'):
    list_hidden_files()