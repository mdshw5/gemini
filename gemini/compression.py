import zlib, cPickle, sqlite3

# http://stackoverflow.com/questions/695794/more-efficient-way-to-pickle-a-string
def pack_blob(obj):
    return sqlite3.Binary(zdumps(obj))

def zdumps(obj):
    return zlib.compress(cPickle.dumps(obj,cPickle.HIGHEST_PROTOCOL),9)

def zloads(zstr):
    return cPickle.loads(zlib.decompress(zstr))

