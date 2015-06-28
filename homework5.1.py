import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
    global crawler_backlog
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")

            #basic page content
            #regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_urls = re.findall(r'href="(.*?)"', content_string)
            regexp_titles = re.findall(r'title="(.*?)"', content_string)

            #new (more) page content
            regexp_bnames = re.findall(r'>(.*?)(</a>|</div>|</span>)', content_string)#button names
            regexp_images = re.findall(r'class="image" src="(.*?)"', content_string)    #all images
            regexp_alts = re.findall(r'alt="(.*?)"', content_string) #all strings starting with 'alt' tag
            '''
            result = regexp_keywords.search(content_string, re.IGNORECASE)  #do not delete

            if result:
                keywords = result.group("keywords")
                print("\nKeywords:\n" + keywords)
'''
            print("\nLinks:")
            for url in regexp_urls:
                print(url)

            print("\nTitles:")
            for title in regexp_titles:
                print(title)

            print("\nButton Names:")
            for bname in regexp_bnames:
                if len(bname)>0:
                    print(bname[0])

            print("\nImage Links:")
            for image in regexp_images:
                print(domain + image)

            print("\nAlts:")
            for alt in regexp_alts:
                print(alt)
    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")
