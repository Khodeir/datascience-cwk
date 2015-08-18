#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree.cElementTree import parse, iterparse
from collections import defaultdict
import pprint, re
class XMLAuditor:
    def __init__(self, file_in, loadall=True):
        self.file_in = file_in
        if loadall:
            self.m = parse(file_in)

    def count(self,xpath,cond=None,mapto=None):
        counts = defaultdict(int)
        for e in self.m.findall(xpath):
            if (not cond) or cond(e):
                counts['total'] += 1
                counts[(mapto and mapto(e)) or e.tag]+=1

        return counts

    def itercount(self,cond=None,mapto=None):
        counts = defaultdict(int)
        for _,e in iterparse(self.file_in):
            if (not cond) or cond(e):
                counts['total'] += 1
                counts[(mapto and mapto(e)) or e.tag]+=1
        return counts
        
def myprint (x):
    if isinstance(x,basestring) or not hasattr(x, '__getitem__'):
        print x,
    else:
        for y in x:
            myprint(y)
        print
def remove(src_string,x):
    return re.sub(x,'',src_string).strip()

arabic_street_types = map(lambda x: unicode('^'+x, 'utf-8'), ['ميدان','طريق','شارع','محور'])
arabic_def_article = unicode('^ال' , 'utf-8')

def clean_arabic_street(src_string):
    result = remove(src_string, arabic_def_article)
    result = remove(result, u'|'.join(arabic_street_types))
    result = remove(result, arabic_def_article)
    return re.sub('\s+',' ', result)

