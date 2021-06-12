# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S, k = map(str, [input(), input()])

i = 0
yes = False
while S:
    match = re.search(str(k), str(S))
    if match:
        print((i+match.start(), i+match.end()-1))
        yes = True
    else:
        break
    S = S[match.start()+1:]
    i += match.start()+1
if yes == False:
    print((-1, -1))
