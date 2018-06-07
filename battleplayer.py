

import sys
import ast
import os

#more input.txt | python battleserver.py --size=5,5 --carrier=0,0,v --play

command = ast.literal_eval(''.join(' '.join(sys.argv[1:]).split('--server-command=')))

#print("python " + command + " --play")

os.system("more input.txt | python " + command + " --play --print")
