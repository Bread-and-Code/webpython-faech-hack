import nntplib
from nntplib import NNTP

s = NNTP('news.gmane.org')
resp, count, first, last, name = s.group('gmane.comp.python.committers')
print ('Group', name, 'has', count, 'articles, range', first, 'to', last)


resp, subs = s.xhdr('subject',first)

for id, sub in subs[-10:]: print (id, sub)

try :
    for id, sub in subs[-10:]: print (id, sub)
except TypeError as e: 
    print(e)
    

print(s.quit())
# NNTP. 