from grab import Grab
import sys
import os
import sys
from bs4 import BeautifulSoup, NavigableString, Tag

def strip_tags(html, invalid_tags):
    soup = BeautifulSoup(html)

    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replaceWith(s)

    return soup

g = Grab()

top = 'http://www.azlyrics.com/g/'

g.go(top + 'guccimane.html')
i = 0
lyrics = []
for elem in g.doc.select('//div/div/a'):
    if elem.text() and i > 3:
        lyrics.append((elem.attr('href')))
        #print '%s' % (elem.attr('href'))
    i = i + 1

f = open('lyrics.txt', 'ab')
for song in lyrics:
    worked = 0
    while worked == 0:
        try:
            g.go(top + song)
            worked = 1
        except:
            print "Unexpected error:", sys.exc_info()[0]
            
    valid = 0
    for elem in g.doc.select('//div/div/div/div'):
        if elem.text() == 'Submit Corrections':
            valid = 0
        if valid == 1:
            html = elem.html()
            #print '%s\n' % (elem.text())
        if elem.text() == 'GUCCI MANE LYRICS':
            valid = 1
    
    soup = strip_tags(html,['i'])
    #print soup.get_text()
    f.write(soup.get_text().encode('ascii', 'ignore').replace('\r\n', os.linesep))

f.close()
