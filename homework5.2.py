import urllib.request
from urllib.error import  URLError
import re
url = "https://restcountries.eu/rest/v1/alpha/"

cc = input("Please input a country code: ")
try:
    print("visiting " + url + cc)
    page = urllib.request.urlopen(url + cc)
    code=page.getcode()
    if(code == 200):
        content=page.read()
        content_string = content.decode("utf-8")
        regexp_name = re.findall(r'"name":"(.*?)"', content_string)
        regexp_capital = re.findall(r'"capital":"(.*?)"', content_string)

        for n in regexp_name:
            print("Country: " + n)
        for c in regexp_capital:
            print("Capital: " + c)
except URLError as e:
        print("error, country code not found")
