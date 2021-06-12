# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

p = re.compile(r'.(#(?:[0-9a-f]{6}|[0-9a-f]{3}))', re.IGNORECASE)
for i in range(int(sys.stdin.readline())):
    
    line = sys.stdin.readline().strip()
    matches = p.findall(line)
    if matches:
        print(*matches, sep='\n')
