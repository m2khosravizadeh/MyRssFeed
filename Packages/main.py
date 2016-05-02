'''
Rss-feed : Summery of the site what you want; news sites, Scientific Sites, Advertisement sites , etc.

*************
The main page
*************
My Resume & Characteristic: 

http://www.hamikar.com/fa/guest/cvlist/cv/96555/%D9%85%D8%AD%D9%85%D8%AF_%D8%AE%D8%B3%D8%B1%D9%88%DB%8C_%D8%B2%D8%A7%D8%AF%D9%87/

https://www.linkedin.com/in/mohammad-khosravizadeh-1943a96b

'''

import httplib
from responsesoup import soupresponse, isolation
from requests.exceptions import ConnectionError, MissingSchema, HTTPError
voroodi = ""
m = ""

voroodi = raw_input('enter a RSS site: ')

m = soupresponse(voroodi)


#print 'natajeh: ','/n',requests.request('GET',voroodi)
if m != "big_bug_soup": 
    for part in isolation(m , 'item'):
        for i in range(len(part.contents)):
            print part.contents[i].string
            
        print ""
    print '\n'"end"
else:
    print "This URL site is not reliable."
    
