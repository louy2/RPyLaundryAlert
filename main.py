import urllib.request
import xml.dom
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == tb)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser(strict=False)

url = "http://www.laundryalert.com/cgi-bin/rpi2012/LMPage?"
hpu = "Login=True"
hpc = urllib.request.urlopen(url+hpu)
