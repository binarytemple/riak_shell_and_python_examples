#!/usr/bin/python 

#ipython tricks
#import readline
#readline.write_history_file('/home/wh/history')

import sys,time,re,string
import optparse
from datetime import date, datetime

def printobj(riak_object):
    print "key:%s" % riak_object.key
    print "data:" 
    for i in riak_object.data.splitlines():
       print ">%s" %i
    print "siblings: %s" % len(foo.siblings)

def append_resolver(riak_object):
    print "resolving siblings for %s" % riak_object.key
    d=[]
    for i in riak_object.siblings:
        d = d + i.data.splitlines()
        #print i.data
        #if i.data is not None and type(i.data) == str and len(i.data) > 0:
        #    d = d + i.data.splitlines()
    res=string.join([i for i in d if i.find('\n') != len(i) -1 ],'\n')  
    riak_object.siblings[0].data = res
    # And finally we set the siblings property to include just the
    # single, resolved sibling
    riak_object.siblings = [riak_object.siblings[0]]
	
def save(bucket,riakobject):
	riakobject.store()


import riak
from riak.content import RiakContent

client = riak.RiakClient(pb_port=8087, protocol='pbc')
bucket=client.bucket('test')
bucket.resolver = append_resolver
#bucket.resolver = riak.resolver.last_written_resolver
bucket.allow_mult

print "current keys in bucket 'test':%s" % bucket.get_keys() 

dt=datetime.now().__str__()
print "creating object with key 'foo' and value '%s'" % dt
foo=bucket.new('foo',data=dt)
printobj(foo)

print "storing object with key 'foo' again"
foo.store()

print "retriving object with key 'foo' again, lets see if it has siblings"

foo=bucket.get('foo')
printobj(foo)

foo.store()
