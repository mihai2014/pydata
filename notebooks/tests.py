from django.test import TestCase

# Create your tests here.

from django.test import Client
#c = Client()
#response = c.post('/login/', {'username': 'john', 'password': 'smith'})
#response.status_code
#200
#response = c.get('/customer/details/')
#response.content

from lxml import html, etree
import re

class Links(TestCase):
    def setUp(self):
        self.c = Client()
        self.failures = []

    def test_all_links(self):
        response = self.c.get('/')
        print(response.status_code)
        index = response.content
        #print(index)
        #response = self.c.get('/about')
        #print(response.status_code)


        doc = html.fromstring(index)
        hrefList =  doc.xpath('/html/body//a')
        for h in hrefList:
            link = h.attrib["href"]
            match_book = re.search("^/book/*",link)
            #verify only local pages
            if(match_book):
                try:
                    response = self.c.get(link)
                    print(response.status_code)
                    if(response.status_code != 200):
                        self.failures.append( {link:str(response.status_code)} )                    
                except Exception as e:
                    self.failures.append({link:str(e)})
                    print(str(e))

        msg="\n\n"
        if(self.failures != {}):
            for item in self.failures:
                msg += str(item) + "\n"

        self.assertEqual(len(self.failures), 0, msg)


