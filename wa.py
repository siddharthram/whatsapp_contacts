#!/usr/bin/python
from html.parser import HTMLParser
import sys
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == 'span':
            #print "in span"
            if (isinstance(attrs,list)):
                for attr in attrs:
                    #print(attr)
                    first, second = attr
                    if first == 'title':
                         #the title tuple also has 'Hi, I'm using whatsapp"
                         pattern = r".*WhatsApp.*"
                         if not re.match(pattern, second):
                             print(second)
            span = True


filename = sys.argv[1]

with open(filename,"r") as file:
    data = file.read()

parser = MyHTMLParser()
parser.feed(data)