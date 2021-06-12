import re

def fun(s):
    # return True if s is a valid email, else return False
    p1 = re.compile('[\w-]+@[\w]+\.[a-zA-Z]+')
    p2 = re.compile('[\w-]+@[a-zA-Z0-9]+\.(.+)')
    try:
        if p1.match(s) and len(p2.findall(s)[0]) <= 3:
            return True        
    except:
        return False  
      
