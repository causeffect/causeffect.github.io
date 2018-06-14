import sys

with open('style') as infile, open('style.css','w') as outfile:
    s = infile.read()
    for i,c in enumerate(s):
        if c == '{':
            outfile.write(' ')
        elif c == '}':
            outfile.write('\n')
        outfile.write(c)
        if c in {';','{'}:
            outfile.write('\n\t')
        elif c == '}':
            outfile.write('\n\n')