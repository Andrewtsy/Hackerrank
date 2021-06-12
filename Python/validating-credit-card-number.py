# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    import re
    n = int(input())
    cc = []
    for i in range(n):
        cc.append(str(input()))
    stdout = []
    p1 = re.compile('[4-6]')
    p2 = re.compile('[^0-9]+')
    p3 = re.compile('[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
    def repeats(string):
        counter = [None, 1]
        for i in string:
            if i == counter[0]:
                counter[1] += 1
            else:
                counter[0] = i
                counter[1] = 1
            if counter[1] == 4:
                return False
        return True
    
    for i in cc:
        if '-' in i:
            if not p3.match(i):
                stdout.append('Invalid')
                continue
            else:
                i = i.replace('-', '')
        if not p2.search(i):
            if p1.match(i):
                if len(i) == 16:
                    if repeats(i):
                        stdout.append('Valid')
                        continue
        stdout.append('Invalid')
    print(*stdout, sep='\n')
                        
                        
                            
