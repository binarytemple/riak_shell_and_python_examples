from riak.content import RiakContent

def append_resolver(riak_object):
	d=""
    for i in riak_object.siblings:
    	d = d + i.data
    riak_object.siblings[0].data = "ballach"
    # And finally we set the siblings property to include just the
    # single, resolved sibling
    riak_object.siblings = [riak_object.siblings[0]]
