# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')

def main():
    html = ''.join([input().strip() for i in range(int(input()))])
    myparser = MyHTMLParser()
    myparser.feed(html)
    myparser.close()

if __name__ =='__main__':
    main()
