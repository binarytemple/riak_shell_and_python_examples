#!/usr/bin/python 

import sys,time,re,string
import optparse
from datetime import date, datetime

def printobj(riak_object):
    from riak.riak_object import ConflictError
    print "siblings: %s" % len(foo.siblings)
    print "key:%s" % riak_object.key
    try:
        print "data:"
        for i in riak_object.data.splitlines():
            print ">%s" %i
    except ConflictError:
        print "object in conflict"
        x=riak_object.siblings
        for i in zip(range(0,len(x)),x):
            print "sibling %s : %s" % ( i[0], i[1] .data) 

import riak
from riak.content import RiakContent

client = riak.RiakClient(pb_port=8087, protocol='pbc')
bucket=client.bucket('test')
bucket.allow_mult

print "Lets create some siblings!"

# 
# Create 20 objects without performing conflict resolution
#
for i in range(0,20):
    dt=datetime.now().__str__()
    print "creating object with key 'foo' and value '%s'" % dt
    try:
        foo=bucket.new('foo',data=dt)
        foo.store()
    except ConflictError:
        print "Conflict error"

print "retriving object with key 'foo' again, lets see if it has siblings"

foo=bucket.get('foo')
printobj(foo)
