# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import re

# match = re.search(r'([a-zA-Z0-9])', input().strip())
# for i in range(len(match.group())):
#     if match[i] == match[i+1]:
#         print(match[i])
#         break
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
