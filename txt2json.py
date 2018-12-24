# reads the name, say F, of a text file, and creates a text file 
# F.json containing one JSON object with three fields:
# {"file_name": "F", "title": "1st line of F", "content": "rest of F lines"}
# any double quote, \n, \r in F is replaced with a space " "
#

import sys

fname = raw_input()
try:
    inf = open(fname,"r")
except IOError:
    print "\nError opening file!"
    sys.exit()

sys.stdout.write('{"title": "')
first = 1
for line in inf.readlines():
    oline = ''
    for ch in line:
        if ch not in '\n\r"': oline += ch
        else: oline += " "
    if first==1:
        sys.stdout.write(oline +'", "Reporter": "')
        first  +=1
    elif first==2:
        sys.stdout.write(oline +'", "content": "')
        first  +=1
    else:
        sys.stdout.write(oline)
sys.stdout.write('"}')

inf.close()
