#!/usr/bin/env python

import glob
#import re
import datetime
import json

from pyquery import PyQuery as pq

def parse_timestamp(age):
    n = int(age.split(' ')[0])
    if 'day' in age:
        delta = datetime.timedelta(days=int(n))
    elif 'hour' in age:
        delta = datetime.timedelta(hours=int(n))
    elif 'minute' in age:
        delta = datetime.timedelta(minutes=int(n))
    elif 'second' in age:
        delta = datetime.timedelta(seconds=int(n))
    else:
        raise Exception('Not sure how to parse age=%s' % age)
    timestamp = ((datetime.datetime.now() + delta) - datetime.datetime(1970, 1, 1)).total_seconds()
    return int(timestamp)

if __name__ == '__main__':
    for filename in glob.glob('data/favorites/*.html'):
        d = pq(filename=filename)
        data = {
            'upvoted': [],
        }
        print filename, len(d('tr'))
        for i, tr in enumerate(d('table#hnmain tr td table tr')):
            if i == 0:
                continue
            tr_d = pq(tr)
            #print tr_d('.title').text()
            #title_text_components = tr_d('.title').text().split('. ', 2)
            if len(tr_d('td')) == 0 or len(tr_d('.morelink')) > 0:
                continue
            print len(tr_d('table')), len(tr_d('.morelink')), pq(tr).html()
            #print title_text_components
            if len(tr_d('.subtext')) > 0: # Detail row.
                row['id'] = int(tr_d('.score').attr('id').split('_', 2)[1])
                row['score'] = int(pq(tr_d('.score')).text().split(' ', 2)[0])
                row['user'] = pq(tr_d('.hnuser')).text()
                row['timestamp'] = parse_timestamp(pq(tr_d('.age')).text())
                data['upvoted'].append(row)
            else:
                row = {
                    #'pos': pq(tr_d('td.title')[0]).text().strip('.'), #title_text_components[0],
                    #'title': pq(tr_d('.title a')[0]).text(), #title_text_components[1],
                    #'link': pq(tr_d('.title a')[0]).attr('href'),
                }
        print data
        break

        #with open(filename, 'r') as fh:
        #    html = fh.read()
        #    #clean_html = re.sub(r'^<html[^>]*>.*?<body[^>]*>(.*)<\/body>.*?<\/html>$', r'\1', html.strip().replace('\n', ''), re.DOTALL)
        #    #print clean_html
        #    d = pq(html)
        #    print len(d('.title'))
        #    break

